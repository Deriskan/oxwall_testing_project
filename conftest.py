import pytest
from selenium import webdriver

from oxwall_helper import OxwallHelper


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://demo.oxwall.com/")
    yield driver
    driver.quit()


@pytest.fixture()
def app(driver):
    return OxwallHelper(driver)


@pytest.fixture()
def login(app):
    app.login_as("demo", "demo")
    yield
    # TODO: sign out



