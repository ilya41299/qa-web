def test_main_page(main_page):
    main_page.open_page()
    main_page.logo.should_be_visible()
    main_page.search.should_be_visible()
    main_page.carousel_banner.should_be_visible()


def test_category_page(category_page):
    category_page.visit_url("/en-gb/catalog/laptop-notebook")
    category_page.category_name.should_be_visible()
    category_page.view_as_list.should_be_visible()
    category_page.view_as_grid.should_be_visible()
    category_page.sort_dropdown.should_be_visible()
    category_page.show_dropdown.should_be_visible()


def test_product_page(product_page):
    product_page.visit_url("/en-gb/product/desktops/mac/imac")
    product_page.add_product_to_cart.should_be_visible()
    product_page.product_description.should_be_visible()
    product_page.add_to_wish_list.should_be_visible()
    product_page.compare_this_product.should_be_visible()
    product_page.product_image.should_be_visible()


def test_admin_login_page(admin_login_page):
    admin_login_page.open_page()
    admin_login_page.email_field.should_be_visible()
    admin_login_page.password_field.should_be_visible()
    admin_login_page.login_btn.should_be_visible()
    admin_login_page.footer.should_be_visible()
    admin_login_page.card_header.should_be_visible()


def test_registration_page(registration_page):
    registration_page.open_page()
    registration_page.first_name.should_be_visible()
    registration_page.last_name.should_be_visible()
    registration_page.email.should_be_visible()
    registration_page.password.should_be_visible()
    registration_page.agree_with_private_policy.should_be_visible()
    registration_page.continue_registration.should_be_visible()
