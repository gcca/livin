import logging
from typing import Final, Iterable, override

from livin.domain.model.location.location import Location
from livin.domain.model.location.repository import LocationRespository

from .repository_pg import RepositoryPg


class LocationRespositoryPg(LocationRespository, RepositoryPg):

    @override
    def Store(self, location: Location) -> None:
        self._ExecuteStore(
            "locations(code, name)", "(%s, %s)", location.code, location.name
        )

    @override
    def Exists(self, code: str) -> bool:
        return self._ExecuteExists(
            tablename="locations", columnname="code", value=code
        )

    @override
    def All(self) -> Iterable[Location]:
        with self._basic_cursor() as cursor:
            max_length: Final[int] = 10000
            try:
                cursor.execute(
                    "SELECT code, name FROM locations LIMIT %d", (max_length,)
                )
                rows = cursor.fetchall()
            except Exception as ex:
                raise RuntimeError("Fetching all locations") from ex
            if len(rows) >= max_length:
                logging.warning(
                    "Retrieving at least max_length=%d rows from locations on 'All'",
                    len(rows),
                )
            return (Location(row[0], row[1]) for row in rows)
