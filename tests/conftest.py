import pytest

from pages.main_page import MainPage
from pages.admin_login_page import AdminLoginPage
from pages.admin_dashboard_page import AdminDashboardPage
from pages.category_page import CategoryPage
from pages.product_page import ProductPage
from pages.registration_page import RegistrationPage


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
