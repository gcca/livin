from fastapi import APIRouter, Depends
from livin.application.users import UsersService
from livin.depends import user_service
from pydantic import BaseModel

router = APIRouter(prefix="/users")


class SignupBody(BaseModel):
    username: str
    password: str


@router.post("/signup")
def Signup(
    body: SignupBody,
    user_service: UsersService = Depends(user_service),
):
    user_service.simple_signup(body.username, body.password)
    return {}
