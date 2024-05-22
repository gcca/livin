from __future__ import annotations

import hashlib
import hmac
from dataclasses import dataclass


@dataclass
class User:
    username: str
    password: str

    @staticmethod
    def MakeSafe(username: str, password: str, key: bytes) -> User:
        password = hmac.new(
            key=key,
            msg=f"{username}:{password}".encode(),
            digestmod=hashlib.sha256,
        ).hexdigest()
        return User(username=username, password=password)
