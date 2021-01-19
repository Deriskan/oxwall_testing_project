from selenium.webdriver.support.wait import WebDriverWait

from pages.locators import PostLocator
from value_objects.user import User


class PostBlock:
    def __init__(self, element, driver):
        self.element = element
        self.wait = WebDriverWait(driver, 5)

    @property
    def text(self):
        return self.element.find_element(*PostLocator.POST_TEXT).text

    @property
    def user(self):
        el = self.element.find_element(*PostLocator.POST_USER)
        real_name = el.text
        username = el.get_attribute("href").split("/")[-1]
        return User(username=username, real_name=real_name)

    @property
    def time(self):
        return self.element.find_element(*PostLocator.POST_TIME).text

    @property
    def like_bt(self):
        return self.element.find_element(*PostLocator.LIKES_BUTTON)

    def delete(self):
        # TODO
        pass

    def add_like(self):
       self.like_bt.click()
