from .component import Component


class Link(Component):
    @property
    def type_of(self) -> str:
        return "link"

    @property
    def link_href(self) -> str:
        self.logger.info(
            "%s: Get href of element %s ('%s', '%s')"
            % (
                self.__class__.__name__,
                self.type_of,
                self.locator["name"],
                self.locator["locator"][1],
            )
        )
        return self._get_element().get_attribute("href")
