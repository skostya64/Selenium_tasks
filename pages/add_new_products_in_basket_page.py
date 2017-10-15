from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class AddNewProductsInBasketPage:

    def __init__(self, driver):
        self.driver = driver

    def open_catalog_b(self):
        self.driver.find_element_by_xpath("//a[@title='Catalog']").click()

    def click_cart_green_duck(self):
        self.driver.find_element_by_xpath("//a[@title='Green Duck']").click()

    def add_to_cart_product(self):
        self.driver.find_element_by_xpath("//button[@name='add_cart_product']").click()

    def count_item_in_basket(self):
        count = int(self.driver.find_element_by_css_selector("span.quantity").text)

    def click_cart_purple_duck(self):
        self.driver.find_element_by_xpath("//a[@title='Purple Duck']").click()

    def click_cart_red_duck(self):
        self.driver.find_element_by_xpath("//a[@title='Red Duck']").click()

    def wait_appear_change_count(self):
        WebDriverWait(self.driver, 10).until(
            lambda x: count + 1 == int(self.driver.find_element_by_css_selector("span.quantity").text))

    def click_cart_basket(self):
        self.driver.find_element_by_id("cart").click()

    def remove_cart_item(self):
        self.driver.find_elements_by_xpath("//button[@name='remove_cart_item']")[0].click()

    def back_to_categories(self):
        self.driver.find_element_by_xpath("//a[contains(., '<< Back')]").click()
