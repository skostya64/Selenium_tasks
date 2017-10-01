from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
wait = driver.implicitly_wait(10)


def there_is_window_other_than(old_windows):
    WebDriverWait(driver, 10).until(
        lambda driver: len(old_windows) != len(driver.window_handles))
    for i in range(len(driver.window_handles)):
        if driver.window_handles[i] not in old_windows:
            return driver.window_handles[i]


def test_create_new_country():
    login(username="admin", password="admin")
    driver.find_element_by_xpath("//span[text()='Countries']").click()
    driver.find_element_by_xpath("//td/a[text()='Ukraine']").click()
    main_window = driver.current_window_handle
    old_windows = driver.window_handles
    for i in range(len(driver.find_elements_by_css_selector("i.fa.fa-external-link"))):
        driver.find_elements_by_css_selector("i.fa.fa-external-link")[i].click()
        new_window = there_is_window_other_than(old_windows)
        driver.switch_to.window(new_window)
        driver.close()
        driver.switch_to.window(main_window)


def login(username, password):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").clear()
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_css_selector("button.btn.btn-default").click()