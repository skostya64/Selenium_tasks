

def test_check_left_panel(app):
    app.login(username="admin", password="admin")
    app.main_page.get_menu_items_list()
    app.main_page.check_all_admin_panel_items()












