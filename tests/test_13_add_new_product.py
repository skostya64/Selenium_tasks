import time


def test_add_new_product_in_basket(app):
    app.login(username="admin", password="admin")
    app.add_new_products_in_basket_page.open_catalog_b()
    app.add_new_products_in_basket_page.count_item_in_basket()
    app.add_new_products_in_basket_page.click_cart_green_duck()
    app.add_new_products_in_basket_page.add_to_cart_product()
    #driver.find_element_by_css_selector("button.featherlight-close-icon.featherlight-close").click()
    app.add_new_products_in_basket_page.wait_appear_change_count()
    app.add_new_products_in_basket_page.count_item_in_basket()
    app.add_new_products_in_basket_page.click_cart_purple_duck()
    app.add_new_products_in_basket_page.add_to_cart_product()
    #driver.find_element_by_css_selector("button.featherlight-close-icon.featherlight-close").click()
    app.add_new_products_in_basket_page.wait_appear_change_count()
    app.add_new_products_in_basket_page.count_item_in_basket()
    app.add_new_products_in_basket_page.click_cart_red_duck()
    app.add_new_products_in_basket_page.add_to_cart_product()
    #driver.find_element_by_css_selector("button.featherlight-close-icon.featherlight-close").click()
    app.add_new_products_in_basket_page.wait_appear_change_count()
    app.add_new_products_in_basket_page.click_cart_basket()
    app.add_new_products_in_basket_page.remove_cart_item()
    time.sleep(1)
    app.add_new_products_in_basket_page.remove_cart_item()
    time.sleep(1)
    app.add_new_products_in_basket_page.remove_cart_item()
    time.sleep(1)
    app.add_new_products_in_basket_page.back_to_categories()



























