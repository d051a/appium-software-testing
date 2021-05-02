from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time


class BaseLocators:
    skip_button_locator = (By.ID, "org.wikipedia:id/fragment_onboarding_skip_button")


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.click_skip_button_if_exists()

    @staticmethod
    def _replace_substring(locator, input_substring, replace_substring):
        by, element_locator = locator[0], locator[1]
        element_locator = str(element_locator).replace(input_substring,
                                                       replace_substring)
        return by, element_locator

    def click_skip_button_if_exists(self):
        try:
            skip_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(BaseLocators.skip_button_locator))
            skip_button.click()
        except TimeoutException:
            pass

    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element with locator: {locator}")

    def find_elements(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elementS with locator: {locator}")

    def check_elements_amount(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator))
        elements = self.driver.find_elements(*locator)
        return len(elements)

    def assert_element_present(self, locator):
        article_title_amount = len(self.driver.find_elements(*locator))
        if article_title_amount:
            return True
        else:
            return False
