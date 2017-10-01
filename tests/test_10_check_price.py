from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)


def test_check_price():
    login(username="admin", password="admin")
    driver.find_element_by_xpath("//i[@class='fa fa-chevron-circle-left']").click()
    p1 = driver.find_element_by_xpath("//div[@class='price-wrapper']/strong[@class='campaign-price']").text
    pr1 = driver.find_element_by_xpath("//div[@class='price-wrapper']/s[@class='regular-price']").text
    driver.find_element_by_xpath("//a[@href='http://localhost/litecart/en/rubber-ducks-c-1/subcategory-c-2/yellow-duck-p-1']").click()
    p2 = driver.find_element_by_xpath("//div[@class='price-wrapper']/strong[@class='campaign-price']").text
    pr2 = driver.find_element_by_xpath("//div[@class='price-wrapper']/s[@class='regular-price']").text
    assert p1 == p2
    assert pr1 == pr2
    driver.quit()


def login(username, password):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").clear()
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_css_selector("button.btn.btn-default").click()