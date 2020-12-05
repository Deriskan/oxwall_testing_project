from selenium.webdriver.common.by import By


class InternalPageLocators:
    ACTIVE_MENU = (By.CSS_SELECTOR, ".ow_menu_wrap .active")
    SIGN_IN_MENU = (By.CSS_SELECTOR, ".ow_signin_label.ow_signin_delimiter")


class MainPageLocators:
    pass


class SignInPageLocators:
    USERNAME_FIELD = (By.NAME, "identity")
    PASSWORD_FIELD = (By.NAME, "password")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, ".ow_positive")


class DashboardPageLocators:

    POST_TEXTFIELD = (By.CLASS_NAME, "ow_newsfeed_status_input")
    SEND_BUTTON = (By.NAME, "save")
    POST_BLOCK = (By.CLASS_NAME, "ow_newsfeed_body")
