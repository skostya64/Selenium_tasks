class CheckPriceYDPage:

    def __init__(self, driver):
        self.driver = driver

    def get_page_yellow_duck(self):
        self.driver.find_element_by_xpath(
            "//a[@href='http://localhost/litecart/en/rubber-ducks-c-1/subcategory-c-2/yellow-duck-p-1']").click()

    def get_compaign_price_yd(self):
        p2 = self.driver.find_element_by_xpath("//div[@class='price-wrapper']/strong[@class='campaign-price']").text
        return p2

    def get_regular_price_yd(self):
        pr2 = self.driver.find_element_by_xpath("//div[@class='price-wrapper']/s[@class='regular-price']").text
        return pr2

