from pages.main import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lib.locators import WelcomeLocator


class WelcomePage(BasePage):
    locator = WelcomeLocator()

    def click_skip_button_if_exists(self):
        skip_button_locator = self.locator.get_locator('skip_button')
        WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(skip_button_locator))
        if self.driver.find_elements(*skip_button_locator):
            self.driver.find_element(*skip_button_locator).\
                click()

    @property
    def skip_button(self):
        skip_button = self.find_element(self.locator.get_locator('skip_button'))
        return skip_button

    def click_on_skip_button(self):
        self.click_on_center_element(self.skip_button)



