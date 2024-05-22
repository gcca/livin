from abc import ABC, abstractmethod


class UsersService(ABC):

    @abstractmethod
    def simple_signup(self, username: str, password: str) -> None: ...
