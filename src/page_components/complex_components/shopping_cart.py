import allure

from src.page_components.button import Button
from src.page_components.title import Title
from src.page_components.page_interface.page_interface import PageInterface
from selenium.webdriver.common.by import By


class ShoppingCart:
    def __init__(self, page_interface: PageInterface) -> None:
        self.page_interface = page_interface
        self.shopping_cart = Button(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//div[@id='header-cart']"),
                "name": "Shopping cart button",
            },
        )

    @allure.step("Открыть корзину")
    def open_shopping_cart(self):
        self.shopping_cart.click()

    def should_contain_product(self, product_name: str):
        with allure.step(f"Проверить, что товар {product_name} добавлен в корзину"):
            Title(
                page_interface=self.page_interface,
                locator={
                    "locator": (
                        By.XPATH,
                        f"//div[@id='header-cart']//td[@class='text-start']//a[text()='{product_name}']",
                    ),
                    "name": f"Product '{product_name}' in shopping cart",
                },
            ).should_be_visible()
