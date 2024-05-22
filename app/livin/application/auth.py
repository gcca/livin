from abc import ABC, abstractmethod


class AuthService(ABC):

    @abstractmethod
    def login(self, username: str, password: str) -> str: ...

    @abstractmethod
    def logout(self, username: str) -> None: ...
