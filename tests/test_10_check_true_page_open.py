

def test_check_page_true(app):
    app.login(username="admin", password="admin")
    app.check_price_page.click_circle_left()
    y1 = app.check_true_page.get_name_product()
    app.check_true_page.click_cart_yellow_duck()
    y2 = app.check_true_page.get_name_product_yellow_duck()
    assert y1 == y2









