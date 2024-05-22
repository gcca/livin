from dataclasses import dataclass


@dataclass
class Credential:
    username: str

    def IsValid(self) -> bool:
        return isinstance(self, ValidCredential)


@dataclass
class ValidCredential(Credential):
    """When credential was found on container."""

    user_id: int


class InvalidCredential(Credential):
    """When credential cannot be retrieved by container."""
