from page_components.button import Button
from page_components.title import Title
from page_components.page_interface.page_interface import PageInterface
from selenium.webdriver.common.by import By


class ProductCart:
    def __init__(self, page_interface: PageInterface) -> None:
        self.page_interface = page_interface

    def get_product_name(self, index: int):
        return Title(
            page_interface=self.page_interface,
            locator={
                "locator": (
                    By.XPATH,
                    f"(//div[@class='product-thumb']//div[@class='description']/h4)[{index}]",
                ),
                "name": "Product name",
            },
        ).text

    def get_product_price(self, index: int):
        return Title(
            page_interface=self.page_interface,
            locator={
                "locator": (
                    By.XPATH,
                    f"(//span[@class='price-new'])[{index}]",
                ),
                "name": "Product price",
            },
        ).text

    def get_product_tax(self, index: int):
        return Title(
            page_interface=self.page_interface,
            locator={
                "locator": (
                    By.XPATH,
                    f"(//span[@class='price-tax'])[{index}]",
                ),
                "name": "Product tax",
            },
        ).text

    def add_product_to_shopping_cart(self, index: int):
        Button(
            page_interface=self.page_interface,
            locator={
                "locator": (
                    By.XPATH,
                    f"(//button[@title='Add to Cart'])[{index}]",
                ),
                "name": "Add product to shopping cart button",
            },
        ).click()

    def add_product_to_wish_list(self, index: int):
        Button(
            page_interface=self.page_interface,
            locator={
                "locator": (
                    By.XPATH,
                    f"(//button[@aria-label='Add to Wish List'])[{index}]",
                ),
                "name": "Add to wish list",
            },
        ).click()

    def compare_this_product(self, index: int):
        Button(
            page_interface=self.page_interface,
            locator={
                "locator": (
                    By.XPATH,
                    f"(//button[@aria-label='Compare this Product'])[{index}]",
                ),
                "name": "Compare this product",
            },
        ).click()
