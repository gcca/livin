from fastapi import status
from fastapi.testclient import TestClient
from livin.domain.model.location.location import Location
from livin.domain.model.user.user import User
from livin.infrastructure.persistence.pg.location import LocationRespositoryPg
from livin.infrastructure.persistence.pg.user import UserRepositoryPg
from livin.main import app
from livin.settings import USER_SAFE_KEY

client = TestClient(app)


def test_create_location():
    resp = client.post("/locations/new", json={"code": "foo", "name": "bar"})
    assert resp.status_code == status.HTTP_201_CREATED
    assert resp.json() == {}


def test_create_voyage():
    UserRepositoryPg().Store(User.MakeSafe("foo", "bar", USER_SAFE_KEY))
    LocationRespositoryPg().Store(Location("12-sur-baz", "12 SUR Baz"))
    LocationRespositoryPg().Store(Location("15-sur-xaz", "15 SUR Xaz"))

    resp = client.post(
        "/voyages/add",
        json={
            "username": "foo",
            "label": "12-to-15",
            "value": 100,
            "lloc": "12-sur-baz",
            "rloc": "15-sur-xaz",
        },
    )
    assert resp.status_code == status.HTTP_201_CREATED
    assert resp.json() == {}
