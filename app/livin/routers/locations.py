from fastapi import APIRouter, Depends, HTTPException, status
from livin.application.locations import LocationsService
from livin.depends import locations_service
from livin.domain.model.location.location import Location
from pydantic import BaseModel, Field

router = APIRouter(prefix="/locations")


class NewBody(BaseModel):
    code: str = Field(title="Location code", description="Must be unique")
    name: str = Field(title="Location name")


@router.post("/new", status_code=status.HTTP_201_CREATED)
def new(
    body: NewBody,
    locations_service: LocationsService = Depends(locations_service),
):
    location = Location(body.code, body.name)
    try:
        locations_service.AddNew(location)
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_412_PRECONDITION_FAILED, detail=str(error)
        )
    return {}
