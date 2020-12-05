from pages.base_page import BasePage
from pages.locators import InternalPageLocators


class InternalPage(BasePage):
    def find_active_menu(self):
        return self.find_element(InternalPageLocators.ACTIVE_MENU)

    def sign_in_menu_click(self):
        # Open sign it window
        sign_in = self.find_visible_element(InternalPageLocators.SIGN_IN_MENU)
        sign_in.click()