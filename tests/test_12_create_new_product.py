from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.implicitly_wait(10)
product_name = "Yoyo"


def test_create_new_product():
    login(username="admin", password="admin")
    driver.find_element_by_xpath("//span[@class='name' and contains(text(), 'Catalog')]").click()
    driver.find_element_by_xpath("//a[@href='http://localhost/litecart/admin/?app=catalog&doc=catalog']").click()
    driver.find_element_by_xpath("//a[@class='btn btn-default' and contains(., ' Add New Product')]").click()
    driver.find_element_by_xpath("//input[@name='name[en]']").clear()
    driver.find_element_by_xpath("//input[@name='name[en]']").send_keys(product_name)
    driver.find_element_by_xpath("//input[@name='code']").clear()
    driver.find_element_by_xpath("//input[@name='code']").send_keys("A0001")
    driver.find_element_by_xpath("//a[text()='Information']").click()
    select_manufactor = Select(driver.find_element_by_name('manufacturer_id'))
    select_manufactor.select_by_value("1")
    driver.find_element_by_name("keywords").send_keys("Fff")
    driver.find_element_by_css_selector(".trumbowyg-editor").send_keys("Aaa")
    driver.find_element_by_xpath("//a[text()='Prices']").click()
    select_purchase = Select(driver.find_element_by_name('purchase_price_currency_code'))
    select_purchase.select_by_value("EUR")
    driver.find_element_by_xpath("//input[@name='prices[USD]']").clear()
    driver.find_element_by_xpath("//input[@name='prices[USD]']").send_keys("10")
    driver.find_element_by_xpath("//button[@name='save']").click()
    driver.find_element_by_xpath("//span[@class='name' and contains(text(), 'Catalog')]").click()
    assert len(driver.find_elements_by_xpath("//a[text()='%s']" % product_name)) > 0


def login(username, password):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").clear()
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_css_selector("button.btn.btn-default").click()