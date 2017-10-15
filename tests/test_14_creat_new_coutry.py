from selenium.webdriver.support.ui import WebDriverWait


def there_is_window_other_than(old_windows):
    WebDriverWait(driver, 10).until(
        lambda driver: len(old_windows) != len(driver.window_handles))
    for i in range(len(driver.window_handles)):
        if driver.window_handles[i] not in old_windows:
            return driver.window_handles[i]


def test_create_new_country(app):
    app.login(username="admin", password="admin")
    driver.find_element_by_xpath("//span[text()='Countries']").click()
    driver.find_element_by_xpath("//td/a[text()='Ukraine']").click()
    main_window = app.driver.current_window_handle
    old_windows = app.driver.window_handles
    for i in range(len(app.driver.find_elements_by_css_selector("i.fa.fa-external-link"))):
        driver.find_elements_by_css_selector("i.fa.fa-external-link")[i].click()
        new_window = there_is_window_other_than(old_windows)
        app.driver.switch_to.window(new_window)
        app.driver.close()
        app.driver.switch_to.window(main_window)
