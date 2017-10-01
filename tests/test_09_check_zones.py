from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)


def test_check_countries():
    login(username="admin", password="admin")
    driver.find_element_by_xpath("//span[@class='name' and contains(text(), 'Countries')]").click()
    country_list = []
    for i in range(len(driver.find_elements_by_xpath("//tr/td[5]/a"))):
        country_list.append(driver.find_elements_by_xpath("//tr/td[5]/a")[i].text)
    assert country_list == sorted(country_list)
    driver.quit()


def test_check_countries_zones():
    login(username="admin", password="admin")
    driver.find_element_by_xpath("//span[@class='name' and contains(text(), 'Countries')]").click()
    country_zones_list = []
    for i in range(len(driver.find_elements_by_xpath("//tr/td[6]"))):
        if int(driver.find_elements_by_xpath("//tr/td[6]")[i].text) > 0:
            driver.find_elements_by_xpath("//tr/td[5]/a")[i].click()
            for i in range(len(driver.find_elements_by_xpath("//tr/td[3]"))):
                country_zones_list.append(driver.find_elements_by_xpath("//tr/td[3]/input")[i].get_attribute("value"))
            assert country_zones_list == sorted(country_zones_list)
            country_zones_list = []
            driver.find_element_by_xpath("//span[@class='name' and contains(text(), 'Countries')]").click()
    driver.quit()


def test_check_geo_zones():
    login(username="admin", password="admin")
    driver.find_element_by_xpath("//span[@class='name' and contains(text(), 'Countries')]").click()
    driver.find_element_by_xpath("//a[@href='http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones']").click()
    zones_list = []
    for i in range(len(driver.find_elements_by_xpath("//tr/td[3]"))):
        zones_list.append(driver.find_elements_by_xpath("//tr/td[3]")[i].text)
    assert zones_list == sorted(zones_list)
    driver.find_element_by_xpath("//span[@class='name' and contains(text(), 'Countries')]").click()
    driver.quit()


def login(username, password):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").clear()
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_css_selector("button.btn.btn-default").click()