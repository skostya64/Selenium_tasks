from selenium.webdriver.support.wait import WebDriverWait


class SelectProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_cart_count(self):
        return int(self.driver.find_element_by_css_selector("span.quantity").text)

    def select_product(self, product):
        self.driver.find_element_by_xpath("//a[@title='%s']" % product).click()

    def wait_until_cart_count_changed(self):
        self.wait.until(lambda x: self.get_cart_count() + 1 == int(
            self.driver.find_element_by_css_selector("span.quantity").text))

    def click_on_label_cart(self):
        self.driver.find_element_by_id("cart").click()

    def click_on_left_menu(self):
        self.driver.find_element_by_xpath("//i[@class='fa fa-chevron-circle-left']").click()

    def verify_stickers(self, i):
        product = self.get_product_list(i)
        if len(product.find_elements_by_css_selector(".sticker")) > 0:
            assert len(product.find_elements_by_css_selector(".sticker")) == 1

    def get_product_list(self, i):
        return self.driver.find_elements_by_css_selector(".product.column.shadow.hover-light")[i]

    def check_stickers_in_products(self, element):
        for i in range(len(element)):
            self.get_product_list(i)
            self.verify_stickers(i)

    def get_product_cart_list(self):
        product_cart = self.driver.find_elements_by_css_selector(".product.column.shadow.hover-light")
        return product_cart
