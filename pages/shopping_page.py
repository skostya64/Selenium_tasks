class ShoppingPage:

    def __init__(self, driver):
        self.driver = driver

    def click_button_remove_product(self):
        self.driver.find_elements_by_xpath("//button[@title='Remove']")[0].click()

    def click_button_back(self):
        self.driver.find_element_by_xpath("//a[contains(., '<< Back')]").click()

    def count_geo_zone(self):
        self.driver.find_element_by_xpath(
            "//a[@href='http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones']").click()