import allure
from pydantic import SecretStr
from selenium import webdriver

from page_components import Button, Input, Title

from pages.base_page import BasePage
from users import User
from selenium.webdriver.common.by import By


class AdminLoginPage(BasePage):
    def __init__(self, driver: webdriver):
        super().__init__(driver=driver)

        self.url = "/administration/"

        self.card_header = Title(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//div[@class='card-header']"),
                "name": "Card header",
            },
        )
        self.footer = Title(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//footer[@id='footer']"),
                "name": "Footer",
            },
        )
        self.login_btn = Button(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//button[@type='submit']"),
                "name": "Login button",
            },
        )
        self.email_field = Input(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//input[@id='input-username']"),
                "name": "Username input",
            },
        )
        self.password_field = Input(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//input[@id='input-password']"),
                "name": "Password input",
            },
        )

    @allure.step("Ввести логин")
    def enter_login(self, login: str):
        self.email_field.clear_and_fill(text=login)

    @allure.step("Ввести пароль")
    def enter_password(self, password: str | SecretStr):
        self.password_field.clear_and_fill(text=password)

    @allure.step("Нажать кнопку логина")
    def click_on_login_button(self):
        self.login_btn.click()

    @allure.step("Пройти аутентификацию")
    def login_in_account(self, user: User):
        self.enter_login(user.login)
        self.enter_password(user.password)
        self.click_on_login_button()
