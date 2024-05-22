from livin.domain.shared.errors import UnknownEntityError


class UnknownLocationError(UnknownEntityError):
    """Raised when cannot find location code."""

    code: str

    __slots__ = ("code",)

    def __init__(self, code: str) -> None:
        self.code = code

    def __str__(self) -> str:
        return f"Unknown location code={self.code}"
