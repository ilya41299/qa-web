from selenium import webdriver

from page_components import Button, Title
from page_components.complex_components.product_cart import ProductCart
from page_components.complex_components.shopping_cart import ShoppingCart
from pages.base_page import BasePage

from selenium.webdriver.common.by import By


class CategoryPage(BasePage):
    def __init__(self, driver: webdriver):
        super().__init__(driver=driver)
        self.category_name = Title(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//div[@id='content']/h2"),
                "name": "Category name",
            },
        )
        self.view_as_list = Button(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//button[@id='button-list']"),
                "name": "View as list",
            },
        )
        self.view_as_grid = Button(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//button[@id='button-grid']"),
                "name": "View as grid",
            },
        )
        self.sort_dropdown = Button(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//select[@id='input-sort']"),
                "name": "Sort dropdown",
            },
        )
        self.show_dropdown = Button(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//select[@id='input-limit']"),
                "name": "Show dropdown",
            },
        )

        self.product_cart = ProductCart(page_interface=self.page_interface)
        self.shopping_cart = ShoppingCart(page_interface=self.page_interface)
