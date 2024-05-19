import os
import pytest
import logging
import datetime
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
    parser.addoption(
        "--log_level",
        default="INFO",
        help="Set log level",
    )


@pytest.fixture(scope="session")
def get_base_url(request) -> str:
    return request.config.getoption("base_url")


@pytest.fixture(scope="function")
def browser(request) -> WebDriver:
    browser_name = request.config.getoption("browser")
    log_level = request.config.getoption("--log_level")

    logger = logging.getLogger(request.node.name)

    if not os.path.exists("logs"):
        os.makedirs("logs")
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info(
        "===> Test %s started at %s" % (request.node.name, datetime.datetime.now())
    )
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
    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name
    logger.info("Browser started at %s" % datetime.datetime.now())
    yield driver
    logger.info(
        "===> Test %s finished at %s" % (request.node.name, datetime.datetime.now())
    )
    driver.quit()
