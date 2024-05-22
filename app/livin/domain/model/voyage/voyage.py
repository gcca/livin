from dataclasses import dataclass

from livin.domain.model.location.location import LoCode


@dataclass
class Voyage:
    username: str
    label: str
    value: int
    lloc: LoCode
    rloc: LoCode
