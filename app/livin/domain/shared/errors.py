class Error(Exception):
    """Error base"""


class ConnectionError(Error):
    """Connection familiy error to db, cache, service, etc."""


class UnknownEntityError(Error):
    """Raised when repository cannot find entity given an unknown criteria."""
