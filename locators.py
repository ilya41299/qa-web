from selenium.webdriver.common.by import By
from typing import TypedDict


class Locator(TypedDict):
    locator: tuple[str, str]
    name: str


class NavbarLocators:
    CURRENCY_DROPDOWN: Locator = {
        "locator": (By.XPATH, "//div[@class='nav float-start']/ul"),
        "name": "Currency dropdown button",
    }
    CURRENCY_EURO: Locator = {
        "locator": (By.XPATH, "//a[@href='EUR']"),
        "name": "Currency euro",
    }
    CURRENCY_POUND_STERLING: Locator = {
        "locator": (By.XPATH, "//a[@href='GBP']"),
        "name": "Currency pound sterling",
    }
    CURRENCY_US_DOLLAR: Locator = {
        "locator": (By.XPATH, "//a[@href='USD']"),
        "name": "Currency US dollar",
    }


class MainPageLocators:
    LOGO: Locator = {
        "locator": (By.XPATH, "//div[@id='logo']//img"),
        "name": "Page logo",
    }
    SEARCH: Locator = {
        "locator": (By.XPATH, "//div[@id='search']/input"),
        "name": "Search input",
    }
    ALERT_TOAST: Locator = {
        "locator": (By.XPATH, "//div[@id='alert']/div"),
        "name": "Alert toast",
    }
    PRODUCT_NAMES: Locator = {
        "locator": (
            By.XPATH,
            "//div[@class='product-thumb']//div[@class='description']/h4",
        ),
        "name": "Products names",
    }
    ADD_TO_SHOPPING_CART: Locator = {
        "locator": (By.XPATH, "//button[@title='Add to Cart']"),
        "name": "Add product to shopping cart buttons",
    }
    SHOPPING_CART: Locator = {
        "locator": (By.XPATH, "//div[@id='header-cart']"),
        "name": "Shopping cart button",
    }
    PRODUCT_NAMES_IN_SHOPPING_CART: Locator = {
        "locator": (By.XPATH, "//div[@id='header-cart']//td[@class='text-start']//a"),
        "name": "Products names in shopping cart",
    }
    PRODUCTS_PRICES: Locator = {
        "locator": (By.XPATH, "//span[@class='price-new']"),
        "name": "Products names in shopping cart",
    }
    PRODUCTS_TAXES: Locator = {
        "locator": (By.XPATH, "//span[@class='price-tax']"),
        "name": "Products names in shopping cart",
    }
    CAROUSEL_BANNER: Locator = {
        "locator": (By.XPATH, "//div[@id='carousel-banner-1']"),
        "name": "Carousel-banner",
    }


class CategoryPageLocators:
    CATEGORY: Locator = {
        "locator": (By.XPATH, "//div[@id='content']/h2"),
        "name": "Category name",
    }
    VIEW_AS_LIST: Locator = {
        "locator": (By.XPATH, "//button[@id='button-list']"),
        "name": "View as list",
    }
    VIEW_AS_GRID: Locator = {
        "locator": (By.XPATH, "//button[@id='button-grid']"),
        "name": "View as grid",
    }
    SORT_DROPDOWN: Locator = {
        "locator": (By.XPATH, "//select[@id='input-sort']"),
        "name": "Sort dropdown",
    }
    SHOW_DROPDOWN: Locator = {
        "locator": (By.XPATH, "//select[@id='input-limit']"),
        "name": "Show dropdown",
    }


class AdminLoginPageLocators:
    CARD_HEADER: Locator = {
        "locator": (By.XPATH, "//div[@class='card-header']"),
        "name": "Card header",
    }
    FOOTER: Locator = {
        "locator": (By.XPATH, "//footer[@id='footer']"),
        "name": "Footer",
    }
    USERNAME: Locator = {
        "locator": (By.XPATH, "//input[@id='input-username']"),
        "name": "Username input",
    }
    PASSWORD: Locator = {
        "locator": (By.XPATH, "//input[@id='input-password']"),
        "name": "Password input",
    }
    LOGIN: Locator = {
        "locator": (By.XPATH, "//button[@type='submit']"),
        "name": "Login button",
    }


class AdminDashboardPageLocators:
    LOGOUT: Locator = {
        "locator": (By.XPATH, "//li[@id='nav-logout']"),
        "name": "Logout button",
    }


class ProductPageLocators:
    ADD_PRODUCT_TO_CART: Locator = {
        "locator": (By.XPATH, "//button[@id='button-cart']"),
        "name": "Add product to cart button",
    }
    PRODUCT_DESCRIPTION: Locator = {
        "locator": (By.XPATH, "//div[@id='tab-description']"),
        "name": "Product description",
    }
    ADD_TO_WISH_LIST: Locator = {
        "locator": (By.XPATH, "//button[@title='Add to Wish List']"),
        "name": "Add to wish list",
    }
    COMPARE_THIS_PRODUCT: Locator = {
        "locator": (By.XPATH, "//button[@title='Compare this Product']"),
        "name": "Compare this product",
    }
    PRODUCT_IMAGE: Locator = {
        "locator": (By.XPATH, "//div[@class='image magnific-popup']/a/img"),
        "name": "Product image",
    }


class RegistrationPageLocators:
    FIRST_NAME: Locator = {
        "locator": (By.XPATH, "//input[@id='input-firstname']"),
        "name": "First name input",
    }
    LAST_NAME: Locator = {
        "locator": (By.XPATH, "//input[@id='input-lastname']"),
        "name": "Last name input",
    }
    EMAIL: Locator = {
        "locator": (By.XPATH, "//input[@id='input-email']"),
        "name": "Email input",
    }
    PASSWORD: Locator = {
        "locator": (By.XPATH, "//input[@id='input-password']"),
        "name": "Password input",
    }
    AGREE_WITH_PRIVATE_POLICY: Locator = {
        "locator": (By.XPATH, "//input[@name='agree']"),
        "name": "Agree too the Privacy Policy toggle",
    }
    CONTINUE: Locator = {
        "locator": (By.XPATH, "//button[@type='submit']"),
        "name": "Continue button",
    }
