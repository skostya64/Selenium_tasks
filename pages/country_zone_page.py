from selenium.webdriver import ActionChains


class CountryZone:

    def __init__(self, driver):
        self.driver = driver

    def get_zone_list(self, i, country_list):
        return country_list.append(self.country_name_list()[i].text)

    def check_all_country_zone(self, country_list):
        for i in range(len(self.country_name_list())):
            self.get_zone_list(i, country_list)
        assert country_list == sorted(country_list)

    def country_name_list(self):
        return self.driver.find_elements_by_xpath("//tr/td[5]/a")

    def verify_all_countries_zones(self, country_zones_list, app):
        for i in range(len(self.driver.find_elements_by_xpath("//tr/td[6]"))):
            if int(self.driver.find_elements_by_xpath("//tr/td[6]")[i].text) > 0:
                element = self.driver.find_elements_by_xpath("//tr/td[5]/a")[i]
                self.driver.execute_script("arguments[0].scrollIntoView()", element)
                element.click()
                for n in range(len(self.get_id_list())):
                    country_zones_list.append(self.get_id_list()[n].text)
                assert country_zones_list == sorted(country_zones_list), "Zone list are " + str(country_zones_list)
                app.main_page.select_countries()

    def verify_geo_zones(self, zones_list):
        for i in range(len(self.get_id_list())):
            zones_list.append(self.get_id_list()[i].text)
        assert zones_list == sorted(zones_list), "Zone list are " + str(zones_list)

    def get_id_list(self):
        return self.driver.find_elements_by_xpath("//table[@id='table-zones']//tr/td[3]/input[@type='hidden']")

