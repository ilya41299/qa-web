from page_components import Button, Input
from page_components.page_interface.page_interface import PageInterface
from selenium.webdriver.common.by import By


class AdminAddCustomer:
    def __init__(self, page_interface: PageInterface) -> None:
        self.page_interface = page_interface
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
        self.password_confirmation = Input(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//input[@id='input-confirm']"),
                "name": "Password confirmation input",
            },
        )
        self.submit = Button(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//button[@type='submit']"),
                "name": "Submit button",
            },
        )

    def add_new_customer(
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
        self.password_confirmation.fill(text=password)
        self.submit.click()
