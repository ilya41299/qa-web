from selenium import webdriver
from selenium.webdriver.common.by import By

from src.page_components import Button, Title
from src.pages.base_page import BasePage


class AdminDashboardPage(BasePage):
    def __init__(self, driver: webdriver):
        super().__init__(driver=driver)
        self.profile = Title(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//li[@id='nav-profile']"),
                "name": "Username in profile",
            },
        )
        self.logout = Button(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//li[@id='nav-logout']"),
                "name": "Logout button",
            },
        )
