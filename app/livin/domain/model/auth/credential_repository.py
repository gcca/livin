from abc import ABC, abstractmethod

from livin.domain.model.auth.credential import Credential
from livin.domain.model.user.user import User


class CredentialRespository(ABC):

    @abstractmethod
    def FindByUser(self, user: User) -> Credential: ...
