from livin.infrastructure.persistence.pg.repository_pg import RepositoryPg
from pytest import fixture


@fixture(scope="module", autouse=True)
def pg():
    with RepositoryPg._basic_cursor() as cursor:
        yield cursor
        cursor.execute(
            "DO $$ DECLARE t RECORD; BEGIN"
            " FOR t IN SELECT tablename FROM pg_tables WHERE schemaname = 'public' AND tablename != 'alembic_version' LOOP"
            " EXECUTE 'TRUNCATE TABLE ' || t.tablename || ' CASCADE;';"
            " END LOOP; END $$;"
        )
        cursor.connection.commit()
