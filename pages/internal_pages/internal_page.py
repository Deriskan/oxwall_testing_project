from pages.base_page import BasePage
from pages.locators import InternalPageLocators
from value_objects.user import User


class InternalPage(BasePage):
    @property
    def active_menu(self):
        return self.find_element(InternalPageLocators.ACTIVE_MENU)

    @property
    def user_menu(self):
        return self.find_element(InternalPageLocators.USER_MENU)

    @property
    def active_user(self):
        real_name = self.user_menu.text
        username = self.user_menu.get_attribute("href").split("/")[-1]
        return User(username=username, real_name=real_name)

    def sign_in_menu_click(self):
        # Open sign it window
        sign_in = self.find_visible_element(InternalPageLocators.SIGN_IN_MENU)
        sign_in.click()