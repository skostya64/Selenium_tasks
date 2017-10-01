from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)


def test_check_stickers():
    login(username="admin", password="admin")
    driver.find_element_by_xpath("//i[@class='fa fa-chevron-circle-left']").click()
    for i in range(len(driver.find_elements_by_css_selector(".product.column.shadow.hover-light"))):
        product = driver.find_elements_by_css_selector(".product.column.shadow.hover-light")[i]
        if len(product.find_elements_by_css_selector(".sticker")) > 0:
            assert len(product.find_elements_by_css_selector(".sticker")) == 1


def login(username, password):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").clear()
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_css_selector("button.btn.btn-default").click()