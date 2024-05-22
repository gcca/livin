from abc import ABC, abstractmethod

from livin.domain.model.location.location import LoCode


class VoyageService(ABC):

    @abstractmethod
    def Add(
        self, username: str, label: str, value: int, lloc: LoCode, rloc: LoCode
    ) -> None: ...
