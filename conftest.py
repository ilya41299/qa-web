import pytest

from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from config import settings


def pytest_addoption(parser):
    parser.addoption(
        "--base_url",
        default=settings.base_url,
        help="Base application url: https://example.com",
    )
    parser.addoption(
        "--browser",
        default="chrome",
        help="Choose browser: chrome or firefox",
    )


@pytest.fixture(scope="session")
def get_base_url(request) -> str:
    return request.config.getoption("base_url")


@pytest.fixture(scope="function")
def browser(request) -> WebDriver:
    browser_name = request.config.getoption("browser")
    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless=new")
        driver = Chrome(options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = Firefox(options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()
