import pytest
from selenium import webdriver

from oxwall_helper import OxwallHelper


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("https://demo.oxwall.com/")
    yield driver
    driver.close()


@pytest.fixture()
def app(driver):
    return OxwallHelper(driver)


@pytest.fixture()
def login(app):
    app.login_as("demo", "demo")
    yield
    # TODO: sign out



