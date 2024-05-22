from abc import ABC, abstractmethod
from typing import Self

from livin.domain.model.location.location import Location


class LocationsService(ABC):

    @abstractmethod
    def AddNew(self, location: Location) -> Self: ...
