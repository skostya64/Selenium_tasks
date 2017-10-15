

def test_check_price_color(app):
    app.login(username="admin", password="admin")
    app.driver.find_element_by_xpath("//i[@class='fa fa-chevron-circle-left']").click()
    color1red = app.driver.find_element_by_xpath("//div[@class='price-wrapper']/strong[@class='campaign-price']").value_of_css_property("color")
    color1black = app.driver.find_element_by_xpath("//div[@class='price-wrapper']/s[@class='regular-price']").value_of_css_property("color")
    app.driver.find_element_by_xpath("//a[@href='http://localhost/litecart/en/rubber-ducks-c-1/subcategory-c-2/yellow-duck-p-1']").click()
    color2red = app.driver.find_element_by_xpath("//div[@class='price-wrapper']/strong[@class='campaign-price']").value_of_css_property("color")
    color2black = app.driver.find_element_by_xpath("//div[@class='price-wrapper']/s[@class='regular-price']").value_of_css_property("color")
    assert color1red == color2red
    assert color1black == color2black


