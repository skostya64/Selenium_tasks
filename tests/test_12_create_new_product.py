

def test_create_new_product(app):
    app.login(username="admin", password="admin")
    app.create_new_product_page.open_catalog()
    app.create_new_product_page.click_list_item_catalog()
    app.create_new_product_page.add_new_product()
    app.add_new_product_page.input_name_product()
    app.add_new_product_page.input_code_product()
    app.add_new_product_page.click_item_menu_information()
    app.add_new_product_page.select_menufactor_name()
    app.add_new_product_page.input_keywords()
    app.add_new_product_page.input_description()
    app.add_new_product_page.click_item_menu_prices()
    app.add_new_product_page.select_purchase_price()
    app.add_new_product_page.input_price()
    app.add_new_product_page.click_button_save()
    app.create_new_product_page.open_catalog()
    app.add_new_product_page.check_expected_new_product_name(product_name="YOYO")















































