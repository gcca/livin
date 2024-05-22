from typing import override

from livin.application.voyage import VoyageService
from livin.domain.model.location.errors import UnknownLocationError
from livin.domain.model.location.location import LoCode
from livin.domain.model.location.repository import LocationRespository
from livin.domain.model.user.errors import UnknownUserError
from livin.domain.model.user.repository import UserRepository
from livin.domain.model.voyage.repository import VoyageRepository
from livin.domain.model.voyage.voyage import Voyage


class VoyageServiceUn(VoyageService):

    location_repository: LocationRespository
    user_repository: UserRepository
    voyage_repository: VoyageRepository

    __slots__ = ("location_repository", "user_repository", "voyage_repository")

    def __init__(
        self,
        location_repository: LocationRespository,
        user_repository: UserRepository,
        voyage_repository: VoyageRepository,
    ) -> None:
        self.location_repository = location_repository
        self.user_repository = user_repository
        self.voyage_repository = voyage_repository

    @override
    def Add(
        self, username: str, label: str, value: int, lloc: LoCode, rloc: LoCode
    ) -> None:
        if not self.user_repository.Exists(username):
            raise UnknownUserError(username)

        if not self.location_repository.Exists(lloc.code):
            raise UnknownLocationError(lloc.code)

        if not self.location_repository.Exists(rloc.code):
            raise UnknownLocationError(rloc.code)

        voyage = Voyage(
            username=username, label=label, value=value, lloc=lloc, rloc=rloc
        )
        self.voyage_repository.Store(voyage)
