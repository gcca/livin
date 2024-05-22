from typing import Self, override

from livin.application.locations import LocationsService
from livin.domain.model.location.location import Location
from livin.domain.model.location.repository import LocationRespository


class LocationsServiceApp(LocationsService):

    location_repository: LocationRespository

    __slots__ = ("location_repository",)

    def __init__(self, location_repository: LocationRespository) -> None:
        self.location_repository = location_repository

    @override
    def AddNew(self, location: Location) -> Self:
        if self.location_repository.Exists(location.code):
            raise ValueError("Location code already exists")
        self.location_repository.Store(location)
        return self
