from selenium import webdriver

from page_components import Button, Input, Title
from page_components.complex_components.product_cart import ProductCart
from page_components.complex_components.shopping_cart import ShoppingCart
from pages.base_page import BasePage

from selenium.webdriver.common.by import By


class RegistrationPage(BasePage):
    def __init__(self, driver: webdriver):
        super().__init__(driver=driver)
        self.url = "/index.php?route=account/register"
        self.first_name = Input(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//input[@id='input-firstname']"),
                "name": "First name input",
            },
        )
        self.last_name = Input(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//input[@id='input-lastname']"),
                "name": "Last name input",
            },
        )
        self.email = Input(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//input[@id='input-email']"),
                "name": "Email input",
            },
        )
        self.password = Input(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//input[@id='input-password']"),
                "name": "Password input",
            },
        )
        self.agree_with_private_policy = Button(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//input[@name='agree']"),
                "name": "Agree too the Privacy Policy toggle",
            },
        )
        self.continue_registration = Button(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//button[@type='submit']"),
                "name": "Continue button",
            },
        )

        self.product_cart = ProductCart(page_interface=self.page_interface)
        self.shopping_cart = ShoppingCart(page_interface=self.page_interface)
