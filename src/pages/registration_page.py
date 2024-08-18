import allure
from selenium import webdriver

from src.page_components import Button, Input, Title
from src.page_components.complex_components.product_cart import ProductCart
from src.page_components.complex_components.shopping_cart import ShoppingCart
from src.pages.base_page import BasePage

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
        self.registration_success_message = Title(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//div[@id='content']/h1"),
                "name": "Registration success message",
            },
        )

        self.product_cart = ProductCart(page_interface=self.page_interface)
        self.shopping_cart = ShoppingCart(page_interface=self.page_interface)

    @allure.step("Зарегистрировать нового пользователя")
    def register_new_user(
        self,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
    ):
        self.first_name.fill(text=first_name)
        self.last_name.fill(text=last_name)
        self.email.fill(text=email)
        self.password.fill(text=password)
        self.agree_with_private_policy.click()
        self.continue_registration.click()
