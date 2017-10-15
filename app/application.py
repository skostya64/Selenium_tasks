from selenium import webdriver
from pages.admin_panel_login_page import AdminPanelLoginPage
from pages.add_to_cart_page import AddToCartPage
from pages.main_page import MainPage
from pages.select_product_page import SelectProductPage
from pages.shopping_page import ShoppingPage
from pages.add_to_user_page import AddToUserPage
from pages.check_price_page import CheckPricePage
from pages.check_price_yd_page import CheckPriceYDPage
from pages.create_new_product_page import CreateNewProductPage
from pages.add_new_product_page import AddNewProductPage
from pages.add_new_products_in_basket_page import AddNewProductsInBasketPage
from pages.check_true_page import CheckTruePage
from pages.login_page import LoginPage
from pages.country_zone_page import CountryZone


class Application:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.implicitly_wait(10)
        self.admin_panel_login_page = AdminPanelLoginPage(self.driver)
        self.add_to_cart_page = AddToCartPage(self.driver)
        self.main_page = MainPage(self.driver)
        self.select_product_page = SelectProductPage(self.driver)
        self.shopping_page = ShoppingPage(self.driver)
        self.add_to_user_page = AddToUserPage(self.driver)
        self.check_price_page = CheckPricePage(self.driver)
        self.check_price_yd_page = CheckPriceYDPage(self.driver)
        self.create_new_product_page = CreateNewProductPage(self.driver)
        self.add_new_product_page = AddNewProductPage(self.driver)
        self.add_new_products_in_basket_page = AddNewProductsInBasketPage(self.driver)
        self.check_true_page = CheckTruePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.country_zone_page = CountryZone(self.driver)

    def quit(self):
        self.driver.quit()

    def login(self, username, password):
        self.admin_panel_login_page.open()
        self.admin_panel_login_page.enter_username(username)
        self.admin_panel_login_page.enter_password(password)
        self.admin_panel_login_page.submit_login()
