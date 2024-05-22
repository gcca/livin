from abc import ABC, abstractmethod

from livin.domain.model.voyage.voyage import Voyage


class VoyageRepository(ABC):

    @abstractmethod
    def Store(self, voyage: Voyage) -> None: ...
