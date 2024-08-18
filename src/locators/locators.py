from typing import TypedDict


class Locator(TypedDict):
    locator: tuple[str, str]
    name: str
