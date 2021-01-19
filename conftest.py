import json
import pytest
import os.path
from selenium import webdriver

from data.random_string import random_string
from db.connector import OxwallDB
from oxwall_helper import OxwallHelper
from pages.internal_pages.login_page import SignInWindow
from pages.internal_pages.main_page import MainPage
from value_objects.user import User

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))


def pytest_addoption(parser):
    parser.addoption(
        "--config", action="store", default="config.json", help="project config file name"
    )
    # parser.addoption(
    #     "--browser", action="store", default="Chrome", help="driver"
    # )


@pytest.fixture(scope="session")
def config(request):
    with open(os.path.join(PROJECT_DIR, request.config.getoption("--config")), encoding="utf8") as f:
        return json.load(f)


@pytest.fixture()
def driver(config, selenium, request):
    # option = request.config.getoption("--browser")
    # if option.lower() == "chrome":
    #     driver = webdriver.Chrome()
    # elif option.lower() == "firefox":
    #     driver = webdriver.Firefox()
    # elif option.lower() == "edge":
    #     driver = webdriver.Edge()
    # else:  #TODO
    #     raise ValueError("Not correct option for browser")
    driver = selenium
    # driver.get(config["base_url"])
    driver.get(request.config.getoption("--base-url"))
    yield driver
    driver.quit()


@pytest.fixture()
def app(driver):
    return OxwallHelper(driver)


@pytest.fixture()
def admin(config):
    user = User(**config["admin"])
    return user


@pytest.fixture()
def logged_user(driver, admin):
    user = admin
    main_page = MainPage(driver)
    main_page.sign_in_menu_click()
    sign_in_page = SignInWindow(driver)
    sign_in_page.input_username(user.username)
    sign_in_page.input_password(user.password)
    sign_in_page.sign_in_click()
    yield user
    # TODO: sign out


@pytest.fixture(scope="session")
def db(config):
    db = OxwallDB(**config["db"])
    yield db
    db.close()


with open(os.path.join(PROJECT_DIR, "data", "user_data_login.json"), encoding="utf8") as f:
    user_list = json.load(f)


@pytest.fixture(params=user_list, ids=[str(u) for u in user_list])
def user(request, db):
    user_data = request.param
    user = User(**user_data)
    db.create_user(user)
    yield user
    db.delete_user(user)


with open(os.path.join(PROJECT_DIR, "data", "post.json"), encoding="utf8") as f:
    post_text_list = json.load(f)

post_text_list.append(random_string(min_len=3, max_len=255))


@pytest.fixture(params=post_text_list)
def post_text(request):
    return request.param
