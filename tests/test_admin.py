import allure

from src.users.users import default_admin
from src.enums.admin_navigation import AdminNavigationTabs, AdminNavigationSubtabs
from utils.fake_data import FakeProductDataFactory, FakeCustomerRegistrationDataFactory


@allure.epic("Страница администратора")
@allure.feature("Раздел товаров")
@allure.story("Действие с товарами")
class TestProducts:
    @allure.title("Добавление товара в магазин")
    def test_add_product(self, admin_login_page, admin_products_page):
        product_data = FakeProductDataFactory.build()
        admin_login_page.open_page()
        admin_login_page.login_in_account(user=default_admin)

        admin_products_page.navigation.open_tab(tab=AdminNavigationTabs.CATALOG)
        admin_products_page.navigation.open_subtab(
            subtab=AdminNavigationSubtabs.CATALOG_PRODUCTS
        )
        admin_products_page.add_new_product(
            name=product_data.name,
            model=product_data.model,
            seo=product_data.seo,
        )

        admin_products_page.alert_toast.should_have_text(
            text="Success: You have modified products!"
        )

    @allure.title("Удаление товара из магазина")
    def test_delete_product(self, admin_login_page, admin_products_page):
        product_data = FakeProductDataFactory.build()
        admin_login_page.open_page()
        admin_login_page.login_in_account(user=default_admin)
        admin_products_page.navigation.open_tab(tab=AdminNavigationTabs.CATALOG)
        admin_products_page.navigation.open_subtab(
            subtab=AdminNavigationSubtabs.CATALOG_PRODUCTS
        )
        admin_products_page.add_new_product(
            name=product_data.name,
            model=product_data.model,
            seo=product_data.seo,
        )

        admin_products_page.navigation.open_subtab(
            subtab=AdminNavigationSubtabs.CATALOG_PRODUCTS
        )
        admin_products_page.delete_product(name=product_data.name)

        admin_products_page.alert_toast.should_have_text(
            text="Success: You have modified products!"
        )


@allure.epic("Страница администратора")
@allure.feature("Раздел пользователей")
@allure.story("Действие с пользователями")
class TestAddCustomer:
    @allure.title("Добавление пользователя")
    def test_add_customer(self, admin_login_page, admin_customers_page):
        customer_data = FakeCustomerRegistrationDataFactory.build()
        admin_login_page.open_page()
        admin_login_page.login_in_account(user=default_admin)

        admin_customers_page.navigation.open_tab(tab=AdminNavigationTabs.CUSTOMERS)
        admin_customers_page.navigation.open_subtab(
            subtab=AdminNavigationSubtabs.CUSTOMERS_CUSTOMERS
        )
        admin_customers_page.add_new_customer(
            first_name=customer_data.first_name,
            last_name=customer_data.last_name,
            email=customer_data.email,
            password=customer_data.password,
        )
        admin_customers_page.alert_toast.should_have_text(
            text="Success: You have modified customers!"
        )
