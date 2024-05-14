from .component import Component


class Link(Component):
    @property
    def type_of(self) -> str:
        return "link"

    @property
    def link_href(self) -> str:
        return self._get_element().get_attribute("href")
