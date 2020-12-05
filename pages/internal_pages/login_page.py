import time
from pages.base_page import BasePage
from pages.locators import SignInPageLocators
from selenium.webdriver.support import expected_conditions as EC


class SignInWindow(BasePage):
    def input_username(self, username):
        username_field = self.find_visible_element(SignInPageLocators.USERNAME_FIELD)
        username_field.clear()
        username_field.send_keys(username)

    def input_password(self, password):
        password_field = self.driver.find_element(*SignInPageLocators.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(password)

    def sign_in_click(self):
        sign_in_button = self.driver.find_element(*SignInPageLocators.SIGN_IN_BUTTON)
        sign_in_button.click()
        # TODO: Explicitly wait:
        time.sleep(2)


