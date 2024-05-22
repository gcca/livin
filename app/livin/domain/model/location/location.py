from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass
class Location:
    code: str
    name: str


class LoCode:

    code: str

    __slots__ = ("code",)

    CODE_RE = re.compile(r"\d{2}-[a-z]{3,15}-\w{1,50}")

    def __init__(self, code: str) -> None:
        self.code = code

    def __str__(self) -> str:
        return self.code

    @staticmethod
    def New(s: str) -> LoCode:
        if not LoCode.CODE_RE.match(s):
            raise ValueError(
                f"Invalid format s={s}. (v.g. 16-sur-localplace12)"
            )
        return LoCode(code=s)
