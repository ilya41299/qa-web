from selenium import webdriver

from page_components import Button, Input

from pages.base_page import BasePage
from page_components.complex_components.admin_add_product import AdminAddProduct
from page_components.complex_components.admin_navigation import AdminNavigation
from selenium.webdriver.common.by import By


class AdminProductsPage(BasePage):
    def __init__(self, driver: webdriver):
        super().__init__(driver=driver)

        self.url = "/administration/"

        self.add_product_btn = Button(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//a[@title='Add New']"),
                "name": "Add product button",
            },
        )
        self.delete_product_btn = Button(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//button[@title='Delete']"),
                "name": "Delete product button",
            },
        )

        self.add_product_modal = AdminAddProduct(page_interface=self.page_interface)
        self.navigation = AdminNavigation(page_interface=self.page_interface)

    def add_new_product(
        self,
        name: str,
        model: str,
        seo: str,
    ):
        self.add_product_btn.click()
        self.add_product_modal.add_new_product(
            name=name,
            model=model,
            seo=seo,
        )

    def delete_product(self, name: str):
        Input(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//input[@id='input-name']"),
                "name": "Product filter name input",
            },
        ).fill(text=name)
        Button(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//button[@id='button-filter']"),
                "name": "Product filter apply button",
            },
        ).click()
        Button(
            page_interface=self.page_interface,
            locator={
                "locator": (
                    By.XPATH,
                    f"//td[contains(text(),'{name}')]/parent::tr//input[@type='checkbox']",
                ),
                "name": f"Product {name} checkbox",
            },
        ).click()
        self.delete_product_btn.click()
        self.page_interface.alert_accept()
