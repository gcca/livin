class UnknownUserError(Exception):
    """Raised when trying to find an user with unkown username."""

    __slots__ = ("username",)

    def __init__(self, username: str) -> None:
        self.username = username

    def __str__(self) -> str:
        return f"No user with username={self.username}"
