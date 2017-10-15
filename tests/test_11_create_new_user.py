import random
import string
import time


def random_email(size=10):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=size)) + "@gmail.com"


def test_check_price(app):
    app.login(username="admin", password="admin")
    app.main_page.open_catalog()
    app.add_to_user_page.add_new_user()
    app.add_to_user_page.enter_first_name()
    app.add_to_user_page.enter_last_name()
    app.add_to_user_page.enter_address1()
    app.add_to_user_page.enter_address2()
    app.add_to_user_page.enter_postcode()
    app.add_to_user_page.enter_city()
    app.add_to_user_page.enter_email(email=random_email())
    app.add_to_user_page.enter_password()
    app.add_to_user_page.enter_confirmed_password()
    time.sleep(1)
    app.add_to_user_page.create_account()
    app.add_to_user_page.return_to_home_page()
    app.add_to_user_page.enter_email(email=random_email())
    app.add_to_user_page.enter_password()
    app.add_to_user_page.click_login()
    app.add_to_user_page.check_expected_text_is_visible()




































