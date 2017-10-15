class CheckTruePage:

    def __init__(self, driver):
        self.driver = driver

    def get_name_product(self):
        y1 = self.driver.find_element_by_xpath("//div[@class='name' and contains(., 'Yellow Duck')]").text
        return y1

    def click_cart_yellow_duck(self):
        self.driver.find_element_by_xpath(
            "//a[@href='http://localhost/litecart/en/rubber-ducks-c-1/subcategory-c-2/yellow-duck-p-1']").click()

    def get_name_product_yellow_duck(self):
        y2 = self.driver.find_element_by_css_selector("h1.title").text
        return y2