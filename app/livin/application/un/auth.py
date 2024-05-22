import datetime
from typing import cast, override

import jwt
from livin.application.auth import AuthService
from livin.domain.model.auth.credential import ValidCredential
from livin.domain.model.auth.credential_repository import CredentialRespository
from livin.domain.model.user.user import User


class JWTAuthService(AuthService):

    credential_repository: CredentialRespository

    SECRET_KEY = (
        "AdIiaeVr7iR6lY_2xoApm4rfOe-l-x5yMhRSp3tWM-f1CuZyp53-PdGMDy3Vet5y"
    )

    def __init__(self, credential_repository: CredentialRespository) -> None:
        self.credential_repository = credential_repository

    @override
    def login(self, username: str, password: str) -> str:
        credential = self.credential_repository.FindByUser(
            user=User.MakeSafe(
                username=username,
                password=password,
                key=app.settings.USER_SAFE_KEY,
            )
        )

        if not credential.IsValid():
            raise ValueError(f"Invalid credential for username={username}")

        payload = {
            "user_id": cast(ValidCredential, credential).user_id,
            "username": credential.username,
            "exp": datetime.datetime.now(datetime.UTC)
            + datetime.timedelta(days=1),
        }

        token = jwt.encode(
            payload=payload, key=self.SECRET_KEY, algorithm="HS256"
        )

        return token

    @override
    def logout(self, username: str) -> None:
        pass
