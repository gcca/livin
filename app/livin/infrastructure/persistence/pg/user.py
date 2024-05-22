from typing import override

from livin.domain.model.user.repository import UserRepository
from livin.domain.model.user.user import User
from livin.infrastructure.persistence.pg.repository_pg import RepositoryPg


class UserRepositoryPg(UserRepository, RepositoryPg):

    @override
    def Store(self, user: User) -> None:
        self._ExecuteStore(
            "users(username, password)",
            "(%s, %s)",
            user.username,
            user.password,
        )

    @override
    def Exists(self, username: str) -> bool:
        return self._ExecuteExists(
            tablename="users", columnname="username", value=username
        )
