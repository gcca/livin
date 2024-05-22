from abc import ABC, abstractmethod

from livin.domain.model.user.user import User


class UserRepository(ABC):

    @abstractmethod
    def Store(self, user: User) -> None: ...

    @abstractmethod
    def Exists(self, username: str) -> bool: ...
