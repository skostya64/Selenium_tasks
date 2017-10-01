from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)


def test_add_new_product_in_basket():
    login(username="admin", password="admin")
    driver.find_element_by_xpath("//a[@title='Catalog']").click()
    count = int(driver.find_element_by_css_selector("span.quantity").text)
    driver.find_element_by_xpath("//a[@title='Green Duck']").click()
    driver.find_element_by_xpath("//button[@name='add_cart_product']").click()
    driver.find_element_by_css_selector("button.featherlight-close-icon.featherlight-close").click()
    WebDriverWait(driver, 10).until(lambda x: count + 1 == int(driver.find_element_by_css_selector("span.quantity").text))
    count = int(driver.find_element_by_css_selector("span.quantity").text)
    driver.find_element_by_xpath("//a[@title='Purple Duck']").click()
    driver.find_element_by_xpath("//button[@name='add_cart_product']").click()
    driver.find_element_by_css_selector("button.featherlight-close-icon.featherlight-close").click()
    WebDriverWait(driver, 10).until(lambda x: count + 1 == int(driver.find_element_by_css_selector("span.quantity").text))
    count = int(driver.find_element_by_css_selector("span.quantity").text)
    driver.find_element_by_xpath("//a[@title='Red Duck']").click()
    driver.find_element_by_xpath("//button[@name='add_cart_product']").click()
    driver.find_element_by_css_selector("button.featherlight-close-icon.featherlight-close").click()
    WebDriverWait(driver, 10).until(lambda x: count + 1 == int(driver.find_element_by_css_selector("span.quantity").text))
    driver.find_element_by_id("cart").click()
    driver.find_elements_by_xpath("//button[@title='Remove']")[0].click()
    time.sleep(1)
    driver.find_elements_by_xpath("//button[@title='Remove']")[0].click()
    time.sleep(1)
    driver.find_elements_by_xpath("//button[@title='Remove']")[0].click()
    time.sleep(1)
    driver.find_element_by_xpath("//a[contains(., '<< Back')]").click()


def login(username, password):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").clear()
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_css_selector("button.btn.btn-default").click()