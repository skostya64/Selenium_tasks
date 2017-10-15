class AddToUserPage:

    def __init__(self, driver):
        self.driver = driver

    def add_new_user(self):
        self.driver.find_element_by_xpath("//a[@href='http://localhost/litecart/en/create_account']").click()

    def enter_first_name(self):
        self.driver.find_element_by_name("firstname").clear()
        self.driver.find_element_by_name("firstname").send_keys("K")

    def enter_last_name(self):
        self.driver.find_element_by_name("lastname").clear()
        self.driver.find_element_by_name("lastname").send_keys("St")

    def enter_address1(self):
        self.driver.find_element_by_name("address1").clear()
        self.driver.find_element_by_name("address1").send_keys("Ch")

    def enter_address2(self):
        self.driver.find_element_by_name("address2").clear()
        self.driver.find_element_by_name("address2").send_keys("Ch")

    def enter_postcode(self):
        self.driver.find_element_by_name("postcode").clear()
        self.driver.find_element_by_name("postcode").send_keys("68")

    def enter_city(self):
        self.driver.find_element_by_name("city").clear()
        self.driver.find_element_by_name("city").send_keys("Ch")

    def enter_email(self, email):
        self.driver.find_element_by_name("email").clear()
        self.driver.find_element_by_name("email").send_keys(email)

    def enter_password(self):
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys("111111")

    def enter_confirmed_password(self):
        self.driver.find_element_by_name("confirmed_password").clear()
        self.driver.find_element_by_name("confirmed_password").send_keys("111111")

    def create_account(self):
        self.driver.find_element_by_name("create_account").click()

    def return_to_home_page(self):
        self.driver.find_element_by_css_selector("li.general-0").click()

    def click_login(self):
        self.driver.find_element_by_name("login").click()

    def check_expected_text_is_visible(self):
        assert len(self.driver.find_elements_by_id("cookies-acceptance")) > 0
