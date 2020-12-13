from custom_wait_condition import find_N_elements_located
from pages.base_page import BasePage
from pages.block_objects.post_block import PostBlock
from pages.internal_pages.internal_page import InternalPage
from pages.locators import DashboardPageLocators


class DashboardPage(InternalPage):
    @property
    def posts(self):
        return [PostBlock(el, self.driver) for el in self.find_all_visible_elements(DashboardPageLocators.POST_BLOCK)]

    @property
    def post_textfield(self):
        return self.find_element(DashboardPageLocators.POST_TEXTFIELD)

    @property
    def send_button(self):
        return self.find_visible_element(DashboardPageLocators.SEND_BUTTON)

    def wait_new_post_appear(self, number_of_posts):
        # posts = driver.find_elements(By.CLASS_NAME,  "ow_newsfeed_body")
        posts = self.wait.until(find_N_elements_located(DashboardPageLocators.POST_BLOCK, number_of_posts + 1),
                                message="New post doesn't appear")

    def create_new_post(self, post_text):
        # Type text of new post
        self.post_textfield.send_keys(post_text)
        # Submit new post
        self.send_button.click()

    def count_posts(self):
        # Count current posts
        number_of_posts = len(self.posts)
        return number_of_posts
