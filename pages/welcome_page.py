from pages.main import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import capabilities


class WelcomeLocators:
    skip_button = (By.ID,
                           "org.wikipedia:id/fragment_onboarding_skip_button")
    skip_button_ios = (By.XPATH, "//XCUIElementTypeButton[@name='Skip']")
    next_button_ios = (By.XPATH, "//XCUIElementTypeStaticText[@name='Next']")


class WelcomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_skip_button_if_exists(self):
        if capabilities.get_platform() == 'ios':
            locator = WelcomeLocators.skip_button_ios
        else:
            locator = WelcomeLocators.skip_button
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(locator))
        if self.driver.find_elements(*locator):
            self.driver.find_element(*locator).\
                click()

