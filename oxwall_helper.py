import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from custom_wait_condition import find_N_elements_located
from pages.locators import DashboardPageLocators


class OxwallHelper:
    def __init__(self, driver):
        self.driver = driver

    def wait_new_post_appear(self, number_of_posts):
        wait = WebDriverWait(self.driver, 5)
        # posts = driver.find_elements(By.CLASS_NAME,  "ow_newsfeed_body")
        posts = wait.until(find_N_elements_located(DashboardPageLocators.POST_BLOCK, number_of_posts + 1),
                           message="New post doesn't appear")

    def create_new_post(self, post_text):
        # Type text of new post
        new_post_textfield = self.driver.find_element(By.CLASS_NAME, "ow_newsfeed_status_input")
        new_post_textfield.send_keys(post_text)
        # Submit new post
        send_button = self.driver.find_element(By.NAME, "save")
        send_button.click()

    def count_posts(self):
        # Count current posts
        posts = self.driver.find_elements(*POST_BLOCK)
        number_of_posts = len(posts)
        return number_of_posts

    def login_as(self, username, password):
        driver = self.driver
        wait = WebDriverWait(driver, 5)
        # Open sign it window
        sign_in = driver.find_element_by_css_selector(".ow_signin_label.ow_signin_delimiter")
        sign_in.click()
        driver.save_screenshot("full_site.png")

        # type username
        username_field = wait.until(EC.visibility_of_element_located((By.NAME, "identity")),
                                    message="No visible username field")
        # username_field = driver.find_element_by_name("identity")
        username_field.clear()
        username_field.send_keys(username)
        # Type password
        password_field = driver.find_element(By.NAME, "password")
        password_field.clear()
        password_field.send_keys(password)
        # Submit form
        sign_in_button = driver.find_element_by_css_selector(".ow_positive")
        sign_in_button.screenshot("sign_in_button.png")
        sign_in_button.click()
        # TODO: Explicitly wait:
        time.sleep(2)
