class CheckPricePage:

    def __init__(self, driver):
        self.driver = driver

    def click_circle_left(self):
        self.driver.find_element_by_xpath("//i[@class='fa fa-chevron-circle-left']").click()

    def get_campaign_price(self):
        p1 = self.driver.find_element_by_xpath("//div[@class='price-wrapper']/strong[@class='campaign-price']").text
        return p1

    def get_regular_price(self):
        pr1 = self.driver.find_element_by_xpath("//div[@class='price-wrapper']/s[@class='regular-price']").text
        return pr1


