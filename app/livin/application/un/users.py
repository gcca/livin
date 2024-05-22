from typing import override

from livin.application.users import UsersService
from livin.domain.model.user.repository import UserRepository
from livin.domain.model.user.user import User


class UsersServiceDbg(UsersService):

    user_repository: UserRepository

    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    @override
    def simple_signup(self, username: str, password: str) -> None:
        user = User.MakeSafe(
            username=username,
            password=password,
            key=app.settings.USER_SAFE_KEY,
        )
        self.user_repository.Store(user=user)
