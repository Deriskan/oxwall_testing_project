from custom_wait_condition import find_N_elements_located
from pages.base_page import BasePage
from pages.locators import DashboardPageLocators


class DashboardPage(BasePage):
    def wait_new_post_appear(self, number_of_posts):
        # posts = driver.find_elements(By.CLASS_NAME,  "ow_newsfeed_body")
        posts = self.wait.until(find_N_elements_located(DashboardPageLocators.POST_BLOCK, number_of_posts + 1),
                                message="New post doesn't appear")

    def create_new_post(self, post_text):
        # Type text of new post
        new_post_textfield = self.driver.find_element(*DashboardPageLocators.POST_TEXTFIELD)
        new_post_textfield.send_keys(post_text)
        # Submit new post
        send_button = self.driver.find_element(*DashboardPageLocators.SEND_BUTTON)
        send_button.click()

    def count_posts(self):
        # Count current posts
        posts = self.driver.find_elements(*DashboardPageLocators.POST_BLOCK)
        number_of_posts = len(posts)
        return number_of_posts
