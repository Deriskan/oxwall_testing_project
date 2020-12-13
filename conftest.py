import pytest
from selenium import webdriver

from oxwall_helper import OxwallHelper
from pages.internal_pages.login_page import SignInWindow
from pages.internal_pages.main_page import MainPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1/oxwall/")
    yield driver
    driver.quit()


@pytest.fixture()
def app(driver):
    return OxwallHelper(driver)


@pytest.fixture()
def logged_user(driver):
    main_page = MainPage(driver)
    main_page.sign_in_menu_click()
    sign_in_page = SignInWindow(driver)
    sign_in_page.input_username("admin")
    sign_in_page.input_password("pass")
    sign_in_page.sign_in_click()
    yield "admin"
    # TODO: sign out


