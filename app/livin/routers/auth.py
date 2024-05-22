from fastapi import APIRouter, Depends, HTTPException, status
from livin.application.auth import AuthService
from livin.depends import auth_service
from pydantic import BaseModel

router = APIRouter(prefix="/auth")


class LoginBody(BaseModel):
    username: str
    password: str


@router.post(path="/login")
def login(
    body: LoginBody,
    auth_service: AuthService = Depends(auth_service),
):
    try:
        return {
            "token": auth_service.login(
                username=body.username, password=body.password
            )
        }
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid username or password",
        ) from error


@router.post(path="/logout")
def logout() -> None:
    return None
