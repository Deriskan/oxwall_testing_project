import json
import pytest
import os.path
from selenium import webdriver

from data.random_string import random_string
from oxwall_helper import OxwallHelper
from pages.internal_pages.login_page import SignInWindow
from pages.internal_pages.main_page import MainPage
from value_objects.user import User

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture()
def driver(selenium):
    # driver = webdriver.Chrome()
    driver = selenium
    driver.get("http://127.0.0.1/oxwall/")
    yield driver
    driver.quit()


@pytest.fixture()
def app(driver):
    return OxwallHelper(driver)


@pytest.fixture()
def logged_user(driver):
    user = User(username="admin", password="pass", real_name="Admin")
    main_page = MainPage(driver)
    main_page.sign_in_menu_click()
    sign_in_page = SignInWindow(driver)
    sign_in_page.input_username(user.username)
    sign_in_page.input_password(user.password)
    sign_in_page.sign_in_click()
    yield user
    # TODO: sign out


with open(os.path.join(PROJECT_DIR, "data", "user_data_login.json"), encoding="utf8") as f:
    user_list = json.load(f)


@pytest.fixture(params=user_list, ids=[str(u) for u in user_list])
def user(request):
    user_data = request.param
    return User(**user_data)


with open(os.path.join(PROJECT_DIR, "data", "post.json"), encoding="utf8") as f:
    post_text_list = json.load(f)

post_text_list.append(random_string(min_len=3, max_len=255))


@pytest.fixture(params=post_text_list)
def post_text(request):
    return request.param
