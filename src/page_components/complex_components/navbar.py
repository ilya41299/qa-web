import allure

from src.page_components.button import Button
from src.page_components.page_interface.page_interface import PageInterface
from selenium.webdriver.common.by import By


class Navbar:
    def __init__(self, page_interface: PageInterface) -> None:
        self.page_interface = page_interface

    def set_currency(self, currency: str):
        with allure.step(f"Установить валюту {currency}"):
            Button(
                page_interface=self.page_interface,
                locator={
                    "locator": (By.XPATH, "//div[@class='nav float-start']/ul"),
                    "name": "Currency dropdown button",
                },
            ).click()
            Button(
                page_interface=self.page_interface,
                locator={
                    "locator": (By.XPATH, f"//a[@href='{currency}']"),
                    "name": f"Currency {currency}",
                },
            ).click()
