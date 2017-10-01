from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)


def test_check_page():
    login(username="admin", password="admin")
    driver.find_element_by_xpath("//i[@class='fa fa-chevron-circle-left']").click()
    y1 = driver.find_element_by_xpath("//div[@class='name']").text
    driver.find_element_by_xpath("//a[@href='http://localhost/litecart/en/rubber-ducks-c-1/subcategory-c-2/yellow-duck-p-1']").click()
    y2 = driver.find_element_by_css_selector("h1.title").text
    assert y1 == y2
    driver.quit()


def login(username, password):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").clear()
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_css_selector("button.btn.btn-default").click()