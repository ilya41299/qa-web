from abc import ABC, abstractmethod
from collections.abc import Callable
from functools import wraps
from typing import ParamSpec, TypeVar
from selenium.webdriver.common.action_chains import ActionChains

from selenium.common import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

from locators import Locator
from page_components.page_interface.page_interface import PageInterface

T = TypeVar("T")
P = ParamSpec("P")


def timeout_wrapper(
    error_msg: str,
) -> [Callable[[Callable[["Component"], None]], Callable[["Component"], None]]]:
    def _timeout_wrapper(
        func: Callable[P, T],
    ) -> Callable[P, T]:
        @wraps(func)
        def wrapper(self: "Component", *args: P.args, **kwargs: P.kwargs) -> T:
            try:
                return func(self, *args, **kwargs)
            except TimeoutException:
                msg = error_msg.format(
                    type_of=self.type_of,
                    locator_name=self.locator["name"],
                    text=kwargs.get("text", ""),
                )
                raise AssertionError(msg) from TimeoutException

        return wrapper

    return _timeout_wrapper


class Component(ABC):
    def __init__(
        self, page_interface: PageInterface, locator: Locator, **kwargs
    ) -> None:
        self._page = page_interface
        self.locator: Locator = {
            "locator": (locator["locator"][0], locator["locator"][1].format(**kwargs)),
            "name": locator["name"],
        }

    def format_locator(self, **kwargs):
        self.locator: Locator = {
            "locator": (
                self.locator["locator"][0],
                self.locator["locator"][1].format(**kwargs),
            ),
            "name": self.locator["name"],
        }

    def _get_element(self) -> WebElement:
        return self._page.get_web_element(locator=self.locator)

    def get_elements(self) -> [WebElement]:
        return self._page.get_web_elements(locator=self.locator)

    @property
    @abstractmethod
    def type_of(self) -> str:
        """Page component type."""

    @property
    def is_visible(self) -> bool:
        return self._get_element().is_displayed()

    @property
    def text(self) -> str:
        return self._get_element().text

    @timeout_wrapper("Проверить что {type_of} '{locator_name}' отображается")
    def should_be_visible(self) -> None:
        self._page.wait.until(EC.visibility_of_element_located(self.locator["locator"]))

    @timeout_wrapper("Проверить что {type_of} '{locator_name}' не отображается")
    def should_not_be_visible(self):
        self._page.wait.until(EC.invisibility_of_element(self.locator["locator"]))

    @timeout_wrapper("Проверить что {type_of} '{locator_name}' имеет текст '{text}'")
    def should_have_text(self, *, text: str = "") -> None:
        self._page.wait.until(
            EC.text_to_be_present_in_element(self.locator["locator"], text)
        )

    def move_to_element(self):
        from selenium.webdriver.common.action_chains import ActionChains

        ActionChains(self._page.driver).move_to_element()

    @timeout_wrapper("Элемент '{locator_name}' не найден на странице")
    def click(self):
        self._page.wait.until(EC.element_to_be_clickable(self.locator["locator"]))
        element = self._get_element()
        ActionChains(self._page.driver).move_to_element(element).click().perform()

    @timeout_wrapper("Элемент '{locator_name}' не кликабелен")
    def should_be_clickable(self):
        self._page.wait.until(EC.element_to_be_clickable(self.locator["locator"]))
