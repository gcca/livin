from typing import override

from livin.domain.model.auth.credential import (
    Credential,
    InvalidCredential,
    ValidCredential,
)
from livin.domain.model.auth.credential_repository import CredentialRespository
from livin.domain.model.user.user import User

from .repository_pg import PgConn, PgCursor, pg_pool


class CredentialRespositoryPg(CredentialRespository):

    @override
    def FindByUser(self, user: User) -> Credential:
        conn: PgConn = pg_pool.getconn()
        cursor: PgCursor
        with conn.cursor() as cursor:
            try:
                cursor.execute(
                    "SELECT id FROM users WHERE username = %s AND password = %s",
                    (user.username, user.password),
                )
            except Exception as ex:
                raise RuntimeError("Fetching credential by slug") from ex
            row = cursor.fetchone()
        pg_pool.putconn(conn)

        if row is None:
            return InvalidCredential(username=user.username)
        else:
            return ValidCredential(username=user.username, user_id=row[0])
