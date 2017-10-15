class AddToCartPage:

    def __init__(self, driver):
        self.driver = driver

    def click_button_add_to_cart(self):
        self.driver.find_element_by_xpath("//button[@name='add_cart_product']").click()

    def close_modal_window(self):
        self.driver.find_element_by_css_selector("button.featherlight-close-icon.featherlight-close").click()


