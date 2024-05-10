from dataclasses import dataclass

from pydantic import SecretStr

from config import settings


@dataclass
class User:
    login: str
    password: SecretStr
    nickname: str

    def __str__(self):
        return self.login


default_admin = User(
    login=settings.admin.login,
    password=settings.admin.password,
    nickname=settings.admin.nickname,
)
