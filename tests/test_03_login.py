

def test_login(app):
    app.login(username="admin", password="admin")
    app.main_page.verify_title_name()





