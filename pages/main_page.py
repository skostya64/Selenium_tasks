import allure
from allure.constants import AttachmentType


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def open_catalog(self):
        self.driver.find_element_by_xpath("//a[@title='Catalog']").click()
        return self

    def verify_title_name(self):
        assert self.driver.title == "My Store"

    def click_left_menu_items(self, i):
        self.driver.find_elements_by_xpath("//li[@id='app-']/a")[i].click()

    def verify_title_h1(self):
        assert len(self.driver.find_elements_by_css_selector("h1")) == 1

    def get_menu_items_list(self):
        return self.driver.find_elements_by_xpath("//li[@id='app-']/a")

    def check_all_admin_panel_items(self):
        items_list = self.get_menu_items_list()
        for i in range(len(items_list)):
            self.click_left_menu_items(i)
            self.verify_title_h1()
            with allure.MASTER_HELPER.step('Admin panel %s' % items_list[i].text):
                allure.MASTER_HELPER.attach('screen', self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)

    def select_countries(self):
        self.driver.find_element_by_xpath("//span[@class='name' and contains(text(), 'Countries')]").click()

    def click_logout(self):
        self.driver.find_element_by_css_selector(".fa.fa-sign-out.fa-lg").click()