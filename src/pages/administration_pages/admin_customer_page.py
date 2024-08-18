import allure
from selenium import webdriver

from src.page_components import Button

from src.pages.base_page import BasePage
from src.page_components.complex_components.admin_add_customer import AdminAddCustomer
from src.page_components.complex_components.admin_navigation import AdminNavigation
from selenium.webdriver.common.by import By


class AdminCustomerPage(BasePage):
    def __init__(self, driver: webdriver):
        super().__init__(driver=driver)
        self.url = "/administration/"
        self.add_customer_btn = Button(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//a[@title='Add New']"),
                "name": "Add customer button",
            },
        )

        self.add_customer_modal = AdminAddCustomer(page_interface=self.page_interface)
        self.navigation = AdminNavigation(page_interface=self.page_interface)

    @allure.step("Зарегистрировать нового пользователя")
    def add_new_customer(
        self,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
    ):
        self.add_customer_btn.click()
        self.add_customer_modal.add_new_customer(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )
