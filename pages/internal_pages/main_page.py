from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def login_as(self, username, password):
        # Open sign it window
        sign_in = self.driver.find_element(MainPageLocators.SIGN_IN_MENU)
        sign_in.click()



