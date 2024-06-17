import allure

from page_components import Button, Input
from page_components.page_interface.page_interface import PageInterface
from selenium.webdriver.common.by import By
from enums.add_product_tabs import AddProductTabs


class AdminAddProduct:
    def __init__(self, page_interface: PageInterface) -> None:
        self.page_interface = page_interface
        self.product_name = Input(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//input[@id='input-name-1']"),
                "name": "Product name",
            },
        )
        self.product_meta_tag = Input(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//input[@id='input-meta-title-1']"),
                "name": "Product meta tag",
            },
        )
        self.submit = Button(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//button[@type='submit']"),
                "name": "Submit",
            },
        )

        self.model = Input(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//input[@id='input-model']"),
                "name": "Model",
            },
        )
        self.seo = Input(
            page_interface=self.page_interface,
            locator={
                "locator": (By.XPATH, "//input[@id='input-keyword-0-1']"),
                "name": "SEO",
            },
        )

    def open_tab(self, tab: AddProductTabs):
        with allure.step(f"Открыть вкладку {tab}"):
            Button(
                page_interface=self.page_interface,
                locator={
                    "locator": (By.XPATH, f"//a[@href='#tab-{tab}']"),
                    "name": f"Catalog {tab}",
                },
            ).click()

    def add_new_product(
        self,
        name: str,
        model: str,
        seo: str,
    ):
        self.product_name.fill(text=name)
        self.product_meta_tag.fill(text=name)
        self.open_tab(tab=AddProductTabs.DATA)
        self.model.fill(text=model)
        self.open_tab(tab=AddProductTabs.SEO)
        self.seo.fill(text=seo)
        self.submit.click()
