from selenium import webdriver

from src.page_components import Button, Image
from src.page_components.complex_components.product_cart import ProductCart
from src.page_components.complex_components.shopping_cart import ShoppingCart
from src.pages.base_page import BasePage

from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def __init__(self, driver: webdriver):
        super().__init__(driver=driver)
        self.add_product_to_cart = Button(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//button[@id='button-cart']"),
                "name": "Add product to cart button",
            },
        )
        self.product_description = Button(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//div[@id='tab-description']"),
                "name": "Product description",
            },
        )
        self.add_to_wish_list = Button(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//button[@title='Add to Wish List']"),
                "name": "Add to wish list",
            },
        )
        self.compare_this_product = Button(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//button[@title='Compare this Product']"),
                "name": "Compare this product",
            },
        )
        self.product_image = Image(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//div[@class='image magnific-popup']/a/img"),
                "name": "Product image",
            },
        )

        self.product_cart = ProductCart(page_interface=self.page_interface)
        self.shopping_cart = ShoppingCart(page_interface=self.page_interface)
