from users import default_admin
import random
import pytest


def test_admin_login_logout(admin_login_page, admin_dashboard_page):
    admin_login_page.open_page()

    admin_login_page.login_in_account(default_admin)
    assert default_admin.nickname in admin_dashboard_page.profile.text
    admin_dashboard_page.logout.click()

    admin_login_page.card_header.should_be_visible()


def test_add_product_to_shopping_cart(main_page):
    main_page.open_page()
    product_position = random.randint(1, 2)

    product_name = main_page.product_cart.get_product_name(index=product_position)
    main_page.product_cart.add_product_to_shopping_cart(index=product_position)

    main_page.shopping_cart.open_shopping_cart()
    main_page.shopping_cart.should_contain_product(product_name=product_name)


@pytest.mark.parametrize(
    ("currency", "currency_symbol"),
    [
        pytest.param(
            "EUR",
            "€",
            id="Currency euro",
        ),
        pytest.param(
            "GBP",
            "£",
            id="Currency pound sterling",
        ),
    ],
)
def test_price_changes_when_changing_currencies(
    currency,
    currency_symbol,
    main_page,
):
    main_page.open_page()
    old_prices = []
    old_taxes = []
    for i in range(1, 4):
        old_prices.append(main_page.product_cart.get_product_price(index=i))
        old_taxes.append(main_page.product_cart.get_product_tax(index=i))
    main_page.navbar.set_currency(currency=currency)
    new_prices = []
    new_taxes = []
    for i in range(1, 4):
        new_prices.append(main_page.product_cart.get_product_price(index=i))
        new_taxes.append(main_page.product_cart.get_product_tax(index=i))

    for old_price, new_price, old_tax, new_tax in zip(
        old_prices, new_prices, old_taxes, new_taxes
    ):
        assert old_price != new_price
        assert old_tax != new_tax
        assert currency_symbol in new_price
        assert currency_symbol in new_tax
