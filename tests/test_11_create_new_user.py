from selenium import webdriver
import random
import string

driver = webdriver.Chrome()
driver.implicitly_wait(10)


def random_email(size=10):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=size)) + "@gmail.com"


def test_check_price():
    login(username="admin", password="admin")
    driver.find_element_by_xpath("//a[@title='Catalog']").click()
    driver.find_element_by_xpath("//a[@href='http://localhost/litecart/en/create_account']").click()
    driver.find_element_by_name("firstname").clear()
    driver.find_element_by_name("firstname").send_keys("K")
    driver.find_element_by_name("lastname").clear()
    driver.find_element_by_name("lastname").send_keys("St")
    driver.find_element_by_name("address1").clear()
    driver.find_element_by_name("address1").send_keys("Ch")
    driver.find_element_by_name("address2").clear()
    driver.find_element_by_name("address2").send_keys("Ch")
    driver.find_element_by_name("postcode").clear()
    driver.find_element_by_name("postcode").send_keys("68")
    driver.find_element_by_name("city").clear()
    driver.find_element_by_name("city").send_keys("Ch")
    driver.find_element_by_name("email").clear()
    driver.find_element_by_name("email").send_keys(random_email())
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys("111111")
    driver.find_element_by_name("confirmed_password").clear()
    driver.find_element_by_name("confirmed_password").send_keys("111111")
    driver.find_element_by_name("create_account").click()
    driver.find_element_by_css_selector("li.general-0").click()
    driver.find_element_by_name("email").clear()
    driver.find_element_by_name("email").send_keys(random_email())
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys("111111")
    driver.find_element_by_name("login").click()
    assert len(driver.find_elements_by_id("cookies-acceptance")) > 0


def login(username, password):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").clear()
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_css_selector("button.btn.btn-default").click()