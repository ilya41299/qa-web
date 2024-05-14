import pytest

from pages.main_page import MainPage
from pages.administration_pages.admin_login_page import AdminLoginPage
from pages.administration_pages.admin_dashboard_page import AdminDashboardPage
from pages.category_page import CategoryPage
from pages.product_page import ProductPage
from pages.registration_page import RegistrationPage
from pages.administration_pages.admin_products_page import AdminProductsPage
from pages.administration_pages.admin_customer_page import AdminCustomerPage


@pytest.fixture()
def main_page(browser) -> MainPage:
    return MainPage(driver=browser)


@pytest.fixture()
def admin_login_page(browser) -> AdminLoginPage:
    return AdminLoginPage(driver=browser)


@pytest.fixture()
def admin_dashboard_page(browser) -> AdminDashboardPage:
    return AdminDashboardPage(driver=browser)


@pytest.fixture()
def category_page(browser) -> CategoryPage:
    return CategoryPage(driver=browser)


@pytest.fixture()
def product_page(browser) -> ProductPage:
    return ProductPage(driver=browser)


@pytest.fixture()
def registration_page(browser) -> RegistrationPage:
    return RegistrationPage(driver=browser)


@pytest.fixture()
def admin_products_page(browser) -> AdminProductsPage:
    return AdminProductsPage(driver=browser)


@pytest.fixture()
def admin_customers_page(browser) -> AdminCustomerPage:
    return AdminCustomerPage(driver=browser)
