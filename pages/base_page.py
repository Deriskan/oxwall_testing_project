from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    def find_element(self, locator):
        el = self.wait.until(EC.presence_of_element_located(locator),
                             message=f"No element with locator='{locator}'")
        return el

    def find_elements(self, locator):
        el = self.wait.until(EC.presence_of_all_elements_located(locator),
                             message=f"No any elements with locator='{locator}'")
        return el

    def find_visible_element(self, locator):
        el = self.wait.until(EC.visibility_of_element_located(locator),
                             message=f"No visible element with locator='{locator}'")
        return el

    def find_all_visible_elements(self, locator):
        els = self.wait.until(EC.visibility_of_all_elements_located(locator),
                             message=f"Not all elements visible with locator={locator}")
        return els
