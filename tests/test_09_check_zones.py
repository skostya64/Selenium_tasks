

def test_check_countries(app):
    app.login(username="admin", password="admin")
    try:
        app.main_page.select_countries()
        country_list = []
        app.country_zone_page.check_all_country_zone(country_list)
    finally:
        app.main_page.click_logout()


def test_check_countries_zones(app):
    app.login(username="admin", password="admin")
    try:
        app.main_page.select_countries()
        country_zones_list = []
        app.country_zone_page.verify_all_countries_zones(country_zones_list, app)
    finally:
        app.main_page.click_logout()


def test_check_geo_zones(app):
    app.login(username="admin", password="admin")
    try:
        app.main_page.select_countries()
        zones_list = []
        app.country_zone_page.verify_geo_zones(zones_list)
    finally:
        app.main_page.click_logout()









