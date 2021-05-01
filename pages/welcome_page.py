from pages.main import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class WelcomeLocators:
    skip_button_locator = (By.ID,
                           "org.wikipedia:id/fragment_onboarding_skip_button")


class WelcomePage(BasePage):
    def __init__(self):
        super().__init__()

    def click_skip_button_if_exists(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(WelcomeLocators.skip_button_locator))
        if self.driver.find_elements(*WelcomeLocators.skip_button_locator):
            self.driver.find_element(*WelcomeLocators.skip_button_locator).\
                click()
