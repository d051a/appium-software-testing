from config import APPIUM_ADDR
from capabilities import capabilities
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestLesson3:
    search_field_locator = (By.ID, "org.wikipedia:id/search_container")
    close_search_button_locator = (By.ID, "org.wikipedia:id/search_close_btn")
    search_results_locator = (By.ID, "org.wikipedia:id/page_list_item_title")
    skip_button_locator = (By.ID, "org.wikipedia:id/fragment_onboarding_skip_button")

    def setup(self):
        self.driver = webdriver.Remote(APPIUM_ADDR, capabilities)
        self.driver.implicitly_wait(5)
        self.click_skip_button_if_exists()

    def teardown(self):
        self.driver.quit()

    def assert_element_has_text(self, locator, text, error):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(locator))
        element = self.driver.find_element(*locator)
        exist_text = element.find_elements(By.XPATH,
                                           f"//*[contains(@text,'{text}')]")
        if not exist_text:
            print(error)
        else:
            return text

    def click_skip_button_if_exists(self):

        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.skip_button_locator))
        if self.driver.find_elements(*self.skip_button_locator):
            self.driver.find_element(*self.skip_button_locator).click()

    def test_ex2(self):
        compire_text = 'Search Wikipedia'
        element_text = self.assert_element_has_text(self.search_field_locator, compire_text,
                                               "error")
        assert element_text == compire_text

    def test_ex3(self):
        search_field = self.driver.find_element(*self.search_field_locator)
        search_field.click()
        search_field.send_keys('appium')
        assert len(self.driver.find_elements(*self.search_results_locator)) > 1
        close_button = self.driver.find_element(*self.close_search_button_locator)
        close_button.click()
        assert len(self.driver.find_elements(*self.search_results_locator)) == 0

    def test_ex4(self):
        search_word = 'Java'
        search_field = self.driver.find_element(*self.search_field_locator)
        search_field.click()
        search_field.send_keys(search_word)
        search_results = self.driver.find_elements(*self.search_results_locator)
        for search_result in search_results:
            assert search_word.lower() in str(search_result.text).lower()
