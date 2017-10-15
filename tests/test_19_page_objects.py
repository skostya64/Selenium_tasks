from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)


def test_add_new_product_in_basket(app):
    app.login(username="admin", password="admin")
    app.main_page.open_catalog()
    app.select_product_page.select_product(product='Green Duck')
    app.add_to_cart_page.click_button_add_to_cart()
    app.add_to_cart_page.close_modal_window()
    #app.select_product_page.wait_until_cart_count_changed()
    app.select_product_page.select_product(product='Purple Duck')
    app.add_to_cart_page.click_button_add_to_cart()
    app.add_to_cart_page.close_modal_window()
    #app.select_product_page.wait_until_cart_count_changed()
    app.select_product_page.select_product(product='Red Duck')
    app.add_to_cart_page.click_button_add_to_cart()
    app.add_to_cart_page.close_modal_window()
    #app.select_product_page.wait_until_cart_count_changed()
    app.select_product_page.click_on_label_cart()
    app.shopping_page.click_button_remove_product()
    time.sleep(1)
    app.shopping_page.click_button_remove_product()
    time.sleep(1)
    #app.shopping_page.click_button_remove_product()
    #time.sleep(1)
    app.shopping_page.click_button_back()
    driver.quit()




















