

def test_check_stickers(app):
    app.login(username="admin", password="admin")
    app.select_product_page.click_on_left_menu()
    product_cart = app.select_product_page.get_product_cart_list()
    app.select_product_page.check_stickers_in_products(product_cart)














