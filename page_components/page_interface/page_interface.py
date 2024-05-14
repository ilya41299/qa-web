from contextlib import contextmanager

from selenium.webdriver import Remote
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from config import settings
from locators import Locator


class PageInterface:
    def __init__(self, driver: Remote = None, timeout=settings.timeout):
        self.driver = driver
        self.wait = WebDriverWait(driver=driver, timeout=timeout)
        self.timeout = timeout

    @contextmanager
    def set_timeout(self, timeout):
        _t = self.timeout
        _wait = self.wait
        self.timeout = timeout
        self.wait = WebDriverWait(driver=self.driver, timeout=timeout)
        yield
        self.timeout = _t
        self.wait = _wait

    @property
    def url(self) -> str:
        return self.driver.current_url

    def visit(self, url: str) -> "PageInterface":
        """Navigate to the given URL."""
        normalized_url = url if url.startswith("http") else (settings.base_url + url)
        self.driver.get(normalized_url)
        return self

    def reload(self) -> "PageInterface":
        """Reload (aka refresh) the current window."""
        self.driver.refresh()
        return self

    def get_web_element(self, locator: Locator) -> WebElement:
        return self.wait.until(EC.presence_of_element_located(locator["locator"]))

    def get_web_elements(self, locator) -> [WebElement]:
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def alert_accept(self) -> None:
        Alert(self.driver).accept()
