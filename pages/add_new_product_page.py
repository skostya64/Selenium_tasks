from selenium.webdriver.support.ui import Select


class AddNewProductPage:

    def __init__(self, driver):
        self.driver = driver

    def input_name_product(self):
        self.driver.find_element_by_xpath("//input[@name='name[en]']").clear()
        self.driver.find_element_by_xpath("//input[@name='name[en]']").send_keys("Yoyo")

    def input_code_product(self):
        self.driver.find_element_by_xpath("//input[@name='code']").clear()
        self.driver.find_element_by_xpath("//input[@name='code']").send_keys("A0001")

    def click_item_menu_information(self):
        self.driver.find_element_by_xpath("//a[text()='Information']").click()

    def select_menufactor_name(self):
        select_manufactor = Select(self.driver.find_element_by_name('manufacturer_id'))
        select_manufactor.select_by_value("1")

    def input_keywords(self):
        self.driver.find_element_by_name("keywords").send_keys("Fff")

    def input_description(self):
        self.driver.find_element_by_css_selector(".trumbowyg-editor").send_keys("Aaa")

    def click_item_menu_prices(self):
        self.driver.find_element_by_xpath("//a[text()='Prices']").click()

    def select_purchase_price(self):
        select_purchase = Select(self.driver.find_element_by_name('purchase_price_currency_code'))
        select_purchase.select_by_value("EUR")

    def input_price(self):
        self.driver.find_element_by_xpath("//input[@name='prices[USD]']").clear()
        self.driver.find_element_by_xpath("//input[@name='prices[USD]']").send_keys("10")

    def click_button_save(self):
        self.driver.find_element_by_xpath("//button[@name='save']").click()

    def check_expected_new_product_name(self, product_name):
        assert len(self.driver.find_elements_by_xpath("//a[text()='%s']" % product_name)) > 0