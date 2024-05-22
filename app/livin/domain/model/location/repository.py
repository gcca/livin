from abc import ABC, abstractmethod
from typing import Iterable

from livin.domain.model.location.location import Location


class LocationRespository(ABC):

    @abstractmethod
    def Store(self, location: Location) -> None: ...

    @abstractmethod
    def Exists(self, code: str) -> bool: ...

    @abstractmethod
    def All(self) -> Iterable[Location]: ...
