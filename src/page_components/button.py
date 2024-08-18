from src.page_components.component import Component


class Button(Component):
    @property
    def type_of(self) -> str:
        return "button"
