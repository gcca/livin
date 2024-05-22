from fastapi import Depends
from livin.application.auth import AuthService
from livin.application.locations import LocationsService
from livin.application.un.auth import JWTAuthService
from livin.application.un.locations import LocationsServiceApp
from livin.application.un.users import UsersServiceDbg
from livin.application.un.voyage import VoyageServiceUn
from livin.application.users import UsersService
from livin.application.voyage import VoyageService
from livin.domain.model.auth.credential_repository import CredentialRespository
from livin.domain.model.location.repository import LocationRespository
from livin.domain.model.user.repository import UserRepository
from livin.domain.model.voyage.repository import VoyageRepository
from livin.infrastructure.persistence.pg.credential_repository import (
    CredentialRespositoryPg,
)
from livin.infrastructure.persistence.pg.location import LocationRespositoryPg
from livin.infrastructure.persistence.pg.user import UserRepositoryPg
from livin.infrastructure.persistence.pg.voyage import VoyageRepositoryPg


def credential_repository() -> CredentialRespository:
    return CredentialRespositoryPg()


def user_repository() -> UserRepository:
    return UserRepositoryPg()


def location_repository() -> LocationRespository:
    return LocationRespositoryPg()


def voyage_repository() -> VoyageRepository:
    return VoyageRepositoryPg()


def auth_service(
    credential_repository: CredentialRespository = Depends(
        credential_repository
    ),
) -> AuthService:
    return JWTAuthService(credential_repository)


def user_service(
    user_repository: UserRepository = Depends(user_repository),
) -> UsersService:
    return UsersServiceDbg(user_repository)


def locations_service(
    location_repository: LocationRespository = Depends(location_repository),
) -> LocationsService:
    return LocationsServiceApp(location_repository)


def voyage_service(
    location_repository: LocationRespository = Depends(location_repository),
    user_repository: UserRepository = Depends(user_repository),
    voyage_repository: VoyageRepository = Depends(voyage_repository),
) -> VoyageService:
    return VoyageServiceUn(
        location_repository, user_repository, voyage_repository
    )
