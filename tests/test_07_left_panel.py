from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)


def test_check_left_panel():
    login(username="admin", password="admin")
    for i in range(len(driver.find_elements_by_xpath("//li[@id='app-']/a"))):
        driver.find_elements_by_xpath("//li[@id='app-']/a")[i].click()
        assert len(driver.find_elements_by_css_selector("h1")) == 1


def login(username, password):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").clear()
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_css_selector("button.btn.btn-default").click()
