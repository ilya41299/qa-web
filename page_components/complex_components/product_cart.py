import allure

from page_components.button import Button
from page_components.title import Title
from page_components.page_interface.page_interface import PageInterface
from selenium.webdriver.common.by import By


class ProductCart:
    def __init__(self, page_interface: PageInterface) -> None:
        self.page_interface = page_interface

    @allure.step("Получить имя продукта")
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

    @allure.step("Получить стоимость продукта")
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

    @allure.step("Получить стоимость продукта с налогом")
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

    @allure.step("Добавить товар в корзину")
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

    @allure.step("Добавить товар в список избранных")
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

    @allure.step("Добавить продукт в список сравнения")
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
