from typing import override

from livin.domain.model.voyage.repository import VoyageRepository
from livin.domain.model.voyage.voyage import Voyage
from livin.infrastructure.persistence.pg.repository_pg import RepositoryPg


class VoyageRepositoryPg(VoyageRepository, RepositoryPg):

    @override
    def Store(self, voyage: Voyage) -> None:
        self._ExecuteStore(
            "voyages(username, label, value, lloc, rloc)",
            "(%s, %s, %s, %s, %s)",
            voyage.username,
            voyage.label,
            voyage.value,
            voyage.lloc.code,
            voyage.rloc.code,
        )
