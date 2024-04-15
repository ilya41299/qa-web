from config import settings
from locators import (
    MainPageLocators,
    CategoryPageLocators,
    ProductPageLocators,
    AdminLoginPageLocators,
    RegistrationPageLocators,
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from yarl import URL


@pytest.mark.parametrize(
    "element",
    [
        pytest.param(
            MainPageLocators.LOGO["locator"], id=MainPageLocators.LOGO["name"]
        ),
        pytest.param(
            MainPageLocators.SEARCH["locator"], id=MainPageLocators.SEARCH["name"]
        ),
        pytest.param(
            MainPageLocators.ADD_TO_SHOPPING_CART["locator"],
            id=MainPageLocators.ADD_TO_SHOPPING_CART["name"],
        ),
        pytest.param(
            MainPageLocators.SHOPPING_CART["locator"],
            id=MainPageLocators.SHOPPING_CART["name"],
        ),
        pytest.param(
            MainPageLocators.CAROUSEL_BANNER["locator"],
            id=MainPageLocators.CAROUSEL_BANNER["name"],
        ),
    ],
)
def test_main_page(
    element: tuple[str, str],
    browser,
    get_base_url,
):
    browser.get(get_base_url)
    WebDriverWait(browser, settings.timeout).until(
        EC.presence_of_element_located(element)
    )


@pytest.mark.parametrize(
    "element",
    [
        pytest.param(
            CategoryPageLocators.CATEGORY["locator"],
            id=CategoryPageLocators.CATEGORY["name"],
        ),
        pytest.param(
            CategoryPageLocators.VIEW_AS_LIST["locator"],
            id=CategoryPageLocators.VIEW_AS_LIST["name"],
        ),
        pytest.param(
            CategoryPageLocators.VIEW_AS_GRID["locator"],
            id=CategoryPageLocators.VIEW_AS_GRID["name"],
        ),
        pytest.param(
            CategoryPageLocators.SORT_DROPDOWN["locator"],
            id=CategoryPageLocators.SORT_DROPDOWN["name"],
        ),
        pytest.param(
            CategoryPageLocators.SHOW_DROPDOWN["locator"],
            id=CategoryPageLocators.SHOW_DROPDOWN["name"],
        ),
    ],
)
def test_category_page(
    element: tuple[str, str],
    browser,
    get_base_url,
):
    browser.get(str(URL(get_base_url).with_path("/en-gb/catalog/laptop-notebook")))
    WebDriverWait(browser, settings.timeout).until(
        EC.presence_of_element_located(element)
    )


@pytest.mark.parametrize(
    "element",
    [
        pytest.param(
            ProductPageLocators.ADD_PRODUCT_TO_CART["locator"],
            id=ProductPageLocators.ADD_PRODUCT_TO_CART["name"],
        ),
        pytest.param(
            ProductPageLocators.PRODUCT_DESCRIPTION["locator"],
            id=ProductPageLocators.PRODUCT_DESCRIPTION["name"],
        ),
        pytest.param(
            ProductPageLocators.ADD_TO_WISH_LIST["locator"],
            id=ProductPageLocators.ADD_TO_WISH_LIST["name"],
        ),
        pytest.param(
            ProductPageLocators.COMPARE_THIS_PRODUCT["locator"],
            id=ProductPageLocators.COMPARE_THIS_PRODUCT["name"],
        ),
        pytest.param(
            ProductPageLocators.PRODUCT_IMAGE["locator"],
            id=ProductPageLocators.PRODUCT_IMAGE["name"],
        ),
    ],
)
def test_product_page(
    element: tuple[str, str],
    browser,
    get_base_url,
):
    browser.get(str(URL(get_base_url).with_path("/en-gb/product/desktops/mac/imac")))
    WebDriverWait(browser, settings.timeout).until(
        EC.presence_of_element_located(element)
    )


@pytest.mark.parametrize(
    "element",
    [
        pytest.param(
            AdminLoginPageLocators.USERNAME["locator"],
            id=AdminLoginPageLocators.USERNAME["name"],
        ),
        pytest.param(
            AdminLoginPageLocators.PASSWORD["locator"],
            id=AdminLoginPageLocators.PASSWORD["name"],
        ),
        pytest.param(
            AdminLoginPageLocators.LOGIN["locator"],
            id=AdminLoginPageLocators.LOGIN["name"],
        ),
        pytest.param(
            AdminLoginPageLocators.FOOTER["locator"],
            id=AdminLoginPageLocators.FOOTER["name"],
        ),
        pytest.param(
            AdminLoginPageLocators.CARD_HEADER["locator"],
            id=AdminLoginPageLocators.CARD_HEADER["name"],
        ),
    ],
)
def test_admin_login_page(
    element: tuple[str, str],
    browser,
    get_base_url,
):
    browser.get(str(URL(get_base_url).with_path("/administration/")))
    WebDriverWait(browser, settings.timeout).until(
        EC.presence_of_element_located(element)
    )


@pytest.mark.parametrize(
    "element",
    [
        pytest.param(
            RegistrationPageLocators.FIRST_NAME["locator"],
            id=RegistrationPageLocators.FIRST_NAME["name"],
        ),
        pytest.param(
            RegistrationPageLocators.LAST_NAME["locator"],
            id=RegistrationPageLocators.LAST_NAME["name"],
        ),
        pytest.param(
            RegistrationPageLocators.EMAIL["locator"],
            id=RegistrationPageLocators.EMAIL["name"],
        ),
        pytest.param(
            RegistrationPageLocators.PASSWORD["locator"],
            id=RegistrationPageLocators.PASSWORD["name"],
        ),
        pytest.param(
            RegistrationPageLocators.AGREE_WITH_PRIVATE_POLICY["locator"],
            id=RegistrationPageLocators.AGREE_WITH_PRIVATE_POLICY["name"],
        ),
        pytest.param(
            RegistrationPageLocators.CONTINUE["locator"],
            id=RegistrationPageLocators.CONTINUE["name"],
        ),
    ],
)
def test_registration_page(
    element: tuple[str, str],
    browser,
    get_base_url,
):
    browser.get(
        str(
            URL(get_base_url).with_path(
                path="/index.php?route=account/register", encoded=True
            )
        )
    )
    WebDriverWait(browser, settings.timeout).until(
        EC.presence_of_element_located(element)
    )
