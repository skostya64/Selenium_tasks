from selenium import webdriver

driver = webdriver.Chrome("C:\\Users\\Kostya\\PycharmProjects\\Selenium_tasks\\chromedriver.exe")


def test_login():
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").clear()
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_css_selector("button.btn.btn-default").click()
    driver.close()