from config import settings
from yarl import URL
from locators import AdminLoginPageLocators, AdminDashboardPageLocators, NavbarLocators
import random
from locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.action_chains import ActionChains


def test_admin_login_logout(browser, get_base_url):
    browser.get(str(URL(get_base_url).with_path("/administration/")))

    browser.find_element(*AdminLoginPageLocators.USERNAME["locator"]).send_keys(
        settings.admin.login
    )
    browser.find_element(*AdminLoginPageLocators.PASSWORD["locator"]).send_keys(
        settings.admin.password.get_secret_value()
    )
    browser.find_element(*AdminLoginPageLocators.LOGIN["locator"]).click()
    WebDriverWait(browser, settings.timeout).until(
        EC.presence_of_element_located(AdminDashboardPageLocators.LOGOUT["locator"])
    )
    browser.find_element(*AdminDashboardPageLocators.LOGOUT["locator"]).click()
    WebDriverWait(browser, settings.timeout).until(
        EC.presence_of_element_located(AdminLoginPageLocators.CARD_HEADER["locator"])
    )


def test_add_product_to_shopping_cart(browser, get_base_url):
    browser.get(get_base_url)
    product_position = random.randint(0, 1)
    product_name = browser.find_elements(*MainPageLocators.PRODUCT_NAMES["locator"])[
        product_position
    ].text
    random_product_to_shopping_cart = browser.find_elements(
        *MainPageLocators.ADD_TO_SHOPPING_CART["locator"]
    )[product_position]
    ActionChains(browser).move_to_element(random_product_to_shopping_cart).perform()
    random_product_to_shopping_cart.click()
    open_shopping_cart_button = browser.find_element(
        *MainPageLocators.SHOPPING_CART["locator"]
    )
    ActionChains(browser).move_to_element(open_shopping_cart_button).perform()
    WebDriverWait(browser, settings.timeout).until(
        EC.invisibility_of_element(MainPageLocators.ALERT_TOAST["locator"])
    )
    open_shopping_cart_button.click()
    assert (
        product_name
        == browser.find_element(
            *MainPageLocators.PRODUCT_NAMES_IN_SHOPPING_CART["locator"]
        ).text
    )


@pytest.mark.parametrize(
    "page_path",
    [
        pytest.param("", id="main page"),
        pytest.param("/en-gb/catalog/desktops/mac", id="catalog page"),
    ],
)
@pytest.mark.parametrize(
    ("currency_symbol", "currency_button_locator"),
    [
        pytest.param(
            "€",
            NavbarLocators.CURRENCY_EURO["locator"],
            id=NavbarLocators.CURRENCY_EURO["name"],
        ),
        pytest.param(
            "£",
            NavbarLocators.CURRENCY_POUND_STERLING["locator"],
            id=NavbarLocators.CURRENCY_POUND_STERLING["name"],
        ),
    ],
)
def test_price_changes_when_changing_currencies(
    page_path: str | None,
    currency_symbol: str,
    currency_button_locator: tuple[str, str],
    browser,
    get_base_url,
):
    browser.get(str(URL(get_base_url).with_path(page_path)))
    old_prices = [
        el.text
        for el in browser.find_elements(*MainPageLocators.PRODUCTS_PRICES["locator"])
    ]
    old_taxes = [
        el.text
        for el in browser.find_elements(*MainPageLocators.PRODUCTS_TAXES["locator"])
    ]
    browser.find_element(*NavbarLocators.CURRENCY_DROPDOWN["locator"]).click()
    browser.find_element(*currency_button_locator).click()
    new_prices = [
        el.text
        for el in browser.find_elements(*MainPageLocators.PRODUCTS_PRICES["locator"])
    ]
    new_taxes = [
        el.text
        for el in browser.find_elements(*MainPageLocators.PRODUCTS_TAXES["locator"])
    ]
    assert (
        currency_symbol
        in browser.find_element(*MainPageLocators.SHOPPING_CART["locator"]).text
    )
    for old_price, new_price, old_tax, new_tax in zip(
        old_prices, new_prices, old_taxes, new_taxes
    ):
        assert old_price != new_price
        assert old_tax != new_tax
        assert currency_symbol in new_price
        assert currency_symbol in new_tax
