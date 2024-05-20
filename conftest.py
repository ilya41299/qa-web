import pytest

from selenium.webdriver import Chrome, Firefox, Remote
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
    parser.addoption(
        "--browser_service",
        default="127.0.0.1",
        help="Remote browser address",
    )
    parser.addoption(
        "--browser_version",
        default="124.0",
        help="Browser version",
    )
    parser.addoption(
        "--vnc",
        action="store_true",
        help="Enable VNC",
    )
    parser.addoption(
        "--video",
        action="store_true",
        help="Enable video recorder",
    )
    parser.addoption(
        "--logs",
        action="store_true",
        help="Store browser logs",
    )


@pytest.fixture(scope="session")
def get_base_url(request) -> str:
    return request.config.getoption("base_url")


@pytest.fixture(scope="function")
def browser(request) -> WebDriver:
    browser_name = request.config.getoption("browser")
    browser_service = request.config.getoption("browser_service")
    browser_version = request.config.getoption("browser_version")
    logs = request.config.getoption("logs")
    video = request.config.getoption("video")
    vnc = request.config.getoption("vnc")

    if settings.is_local:
        if browser_name == "chrome":
            options = ChromeOptions()
            options.add_argument("--headless=new")
            driver = Chrome(options=options)
        elif browser_name == "firefox":
            options = FirefoxOptions()
            options.add_argument("--headless")
            driver = Firefox(options=options)
        else:
            raise pytest.UsageError("--browser_name should be chrome or firefox")
        driver.set_window_size(1920, 1080)
    else:
        if browser_name == "chrome":
            options = ChromeOptions()
        elif browser_name == "firefox":
            options = FirefoxOptions()
        else:
            raise pytest.UsageError("--browser_name should be chrome or firefox")
        caps = {
            "browserName": browser_name,
            "browserVersion": browser_version,
            "selenoid:options": {
                "enableVNC": vnc,
                "name": request.node.name,
                "screenResolution": "1920x1080",
                "enableVideo": video,
                "enableLog": logs,
            },
        }
        for k, v in caps.items():
            options.set_capability(k, v)
        driver = Remote(
            command_executor=f"http://{browser_service}:4444/wd/hub", options=options
        )
    yield driver
    driver.quit()
