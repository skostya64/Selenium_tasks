from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)


def test_check_price_color():
    login(username="admin", password="admin")
    driver.find_element_by_xpath("//i[@class='fa fa-chevron-circle-left']").click()
    color1red = driver.find_element_by_xpath("//div[@class='price-wrapper']/strong[@class='campaign-price']").value_of_css_property("color")
    color1black = driver.find_element_by_xpath("//div[@class='price-wrapper']/s[@class='regular-price']").value_of_css_property("color")
    driver.find_element_by_xpath("//a[@href='http://localhost/litecart/en/rubber-ducks-c-1/subcategory-c-2/yellow-duck-p-1']").click()
    color2red = driver.find_element_by_xpath("//div[@class='price-wrapper']/strong[@class='campaign-price']").value_of_css_property("color")
    color2black = driver.find_element_by_xpath("//div[@class='price-wrapper']/s[@class='regular-price']").value_of_css_property("color")
    assert color1red == color2red
    assert color1black == color2black
    driver.quit()


def login(username, password):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").clear()
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_css_selector("button.btn.btn-default").click()

