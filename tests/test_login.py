from pages.internal_pages.dashbord_page import DashboardPage
from pages.internal_pages.login_page import SignInWindow
from pages.internal_pages.main_page import MainPage


def test_positive_login(driver, user):
    main_page = MainPage(driver)
    main_page.sign_in_menu_click()
    sign_in_page = SignInWindow(driver)
    # sign_in_page.username_field.send_keys("demo")
    sign_in_page.input_username(user.username)
    sign_in_page.input_password(user.password)
    sign_in_page.sign_in_click()
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.active_menu.text == "DASHBOARD"
    assert dashboard_page.active_user == user
