from .component import Component


class Title(Component):
    @property
    def type_of(self) -> str:
        return "title"
