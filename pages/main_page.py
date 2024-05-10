from selenium import webdriver

from page_components import Input, Title
from page_components.complex_components.product_cart import ProductCart
from page_components.complex_components.shopping_cart import ShoppingCart
from page_components.complex_components.navbar import Navbar
from pages.base_page import BasePage

from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def __init__(self, driver: webdriver):
        super().__init__(driver=driver)

        self.search = Input(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//div[@id='search']/input"),
                "name": "Search input",
            },
        )
        self.alert_toast = Title(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//div[@id='alert']/div"),
                "name": "Alert toast",
            },
        )
        self.logo = Title(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//div[@id='logo']//img"),
                "name": "Page logo",
            },
        )
        self.carousel_banner = Title(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//div[@id='carousel-banner-1']"),
                "name": "Carousel-banner",
            },
        )
        self.navbar = Navbar(page_interface=self.page_interface)
        self.product_cart = ProductCart(page_interface=self.page_interface)
        self.shopping_cart = ShoppingCart(page_interface=self.page_interface)
