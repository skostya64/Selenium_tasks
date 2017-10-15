

def test_check_price(app):
    app.login(username="admin", password="admin")
    app.check_price_page.click_circle_left()
    p1 = app.check_price_page.get_campaign_price()
    pr1 = app.check_price_page.get_regular_price()
    app.check_price_yd_page.get_page_yellow_duck()
    p2 = app.check_price_yd_page.get_compaign_price_yd()
    pr2 = app.check_price_yd_page.get_regular_price_yd()
    assert p1 == p2
    assert pr1 == pr2





















