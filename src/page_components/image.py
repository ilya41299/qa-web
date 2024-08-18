from src.page_components.component import Component


class Image(Component):
    @property
    def type_of(self) -> str:
        return "image"
