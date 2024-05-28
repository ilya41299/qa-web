import allure

from page_components.button import Button
from page_components.page_interface.page_interface import PageInterface
from selenium.webdriver.common.by import By
from enums.admin_navigation import AdminNavigationSubtabs, AdminNavigationTabs


class AdminNavigation:
    def __init__(self, page_interface: PageInterface) -> None:
        self.page_interface = page_interface

    def open_tab(self, tab: AdminNavigationTabs):
        with allure.step(f"Открыть вкладку {tab}"):
            Button(
                page_interface=self.page_interface,
                locator={
                    "locator": (By.XPATH, f"//li[@id='menu-{tab}']"),
                    "name": f"Catalog {tab} button",
                },
            ).click()

    def open_subtab(self, subtab: AdminNavigationSubtabs):
        with allure.step(f"Открыть раздел {subtab}"):
            Button(
                page_interface=self.page_interface,
                locator={
                    "locator": (By.XPATH, f"//a[contains(@href,'{subtab}')]"),
                    "name": f"Catalog {subtab} button",
                },
            ).click()
