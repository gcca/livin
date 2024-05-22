from contextlib import contextmanager
from typing import Iterator, Optional, Tuple, TypeAlias

import psycopg2.extensions
import psycopg2.pool

PgPool: TypeAlias = psycopg2.pool.AbstractConnectionPool
PgConn: TypeAlias = psycopg2.extensions.connection
PgCursor: TypeAlias = psycopg2.extensions.cursor

pg_pool: PgPool = psycopg2.pool.SimpleConnectionPool(
    minconn=1,
    maxconn=20,
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432",
    database="livin",
)


class RepositoryPg:

    @staticmethod
    @contextmanager
    def _basic_cursor() -> Iterator[PgCursor]:
        conn: PgConn = RepositoryPg._getconn()
        cursor: PgCursor = conn.cursor()
        try:
            yield cursor
        finally:
            cursor.close()
            RepositoryPg._putconn(conn=conn)

    @staticmethod
    def _ExecuteStore(tabledef: str, valuesdef: str, *args):
        with RepositoryPg._basic_cursor() as cursor:
            try:
                cursor.execute(
                    f"INSERT INTO {tabledef} VALUES {valuesdef}",
                    args,
                )
                cursor.connection.commit()
            except Exception as ex:
                raise RuntimeError(
                    f"Storing {tabledef} with {valuesdef}={args}"
                ) from ex

    @staticmethod
    def _ExecuteExists(tablename: str, columnname: str, value: str) -> bool:
        with RepositoryPg._basic_cursor() as cursor:
            try:
                cursor.execute(
                    f"SELECT EXISTS (SELECT 1 FROM {tablename} WHERE {columnname} = %s)",
                    (value,),
                )
                row: Optional[Tuple[bool]] = cursor.fetchone()
            except Exception as ex:
                raise RuntimeError(
                    f"Check {tablename}.{columnname}={value} exists"
                ) from ex
            return (row is not None) and (row[0])

    @staticmethod
    def _getconn() -> PgConn:
        return pg_pool.getconn()

    @staticmethod
    def _putconn(conn: PgConn) -> None:
        pg_pool.putconn(conn=conn)
