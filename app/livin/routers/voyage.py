from fastapi import APIRouter, Depends, HTTPException, status
from livin.application.voyage import VoyageService
from livin.depends import voyage_service
from livin.domain.model.location.location import LoCode
from livin.domain.shared.errors import UnknownEntityError
from pydantic import BaseModel

router = APIRouter(prefix="/voyages")


class AddBody(BaseModel):
    username: str
    label: str
    value: int
    lloc: str
    rloc: str


@router.post("/add", status_code=status.HTTP_201_CREATED)
def add(
    body: AddBody, voyage_service: VoyageService = Depends(voyage_service)
):
    lloc = LoCode.New(body.lloc)
    rloc = LoCode.New(body.rloc)
    try:
        voyage_service.Add(body.username, body.label, body.value, lloc, rloc)
    except UnknownEntityError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(error)
        )
    return {}
