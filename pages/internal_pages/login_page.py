import time
from pages.base_page import BasePage
from pages.locators import SignInPageLocators
from selenium.webdriver.support import expected_conditions as EC


class SignInWindow(BasePage):
    # username_field = Find(*SignInPageLocators.USERNAME_FIELD)

    @property
    def username_field(self):
        return self.find_visible_element(SignInPageLocators.USERNAME_FIELD)

    @property
    def password_field(self):
        return self.find_visible_element(SignInPageLocators.PASSWORD_FIELD)

    @property
    def sign_in(self):
        return self.find_visible_element(SignInPageLocators.SIGN_IN_BUTTON)

    def input_username(self, username):
        self.username_field.clear()
        self.username_field.send_keys(username)

    def input_password(self, password):
        self.password_field.clear()
        self.password_field.send_keys(password)

    def sign_in_click(self):
        self.sign_in.click()
        # TODO: Explicitly wait:
        time.sleep(2)


