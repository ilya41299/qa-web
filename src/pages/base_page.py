import allure
from selenium.webdriver import Remote

from config import settings
from src.page_components import Title
from selenium.webdriver.common.by import By
from src.page_components.page_interface.page_interface import PageInterface


class BasePage:
    def __init__(self, driver: Remote):
        self.page_interface = PageInterface(driver)
        self.url = settings.base_url

        self.alert_toast = Title(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//div[@id='alert']/div"),
                "name": "Alert toast",
            },
        )

    def open_page(self):
        with allure.step(f'Перейти на "{self.url}"'):
            self.page_interface.visit(self.url)

    def visit_url(self, url: str):
        with allure.step(f'Перейти на "{url}"'):
            self.page_interface.visit(url)

    def reload_page(self):
        with allure.step(f'Обновить страницу "{self.url}"'):
            self.page_interface.reload()
