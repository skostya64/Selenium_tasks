class CreateNewProductPage:

    def __init__(self, driver):
        self.driver = driver

    def open_catalog(self):
        self.driver.find_element_by_xpath("//span[@class='name' and contains(text(), 'Catalog')]").click()

    def click_list_item_catalog(self):
        self.driver.find_element_by_xpath(
            "//a[@href='http://localhost/litecart/admin/?app=catalog&doc=catalog']").click()

    def add_new_product(self):
        self.driver.find_element_by_xpath("//a[@href='http://localhost/litecart/admin/?category_id=0&app=catalog&doc=edit_product']").click()

