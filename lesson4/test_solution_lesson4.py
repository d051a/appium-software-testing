from config import APPIUM_ADDR
from capabilities import capabilities
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
import time


class TestLesson4:
    search_field_locator = (By.ID, "org.wikipedia:id/search_container")
    close_search_button_locator = (By.ID, "org.wikipedia:id/search_close_btn")
    search_results_locator = (By.ID, "org.wikipedia:id/page_list_item_title")
    skip_button_locator = (By.ID, "org.wikipedia:id/fragment_onboarding_skip_button")
    article_list_title_locator = (By.XPATH,
                                  "//android.widget.TextView[contains(@resource-id, 'org.wikipedia:id/page_list_item_title')]")
    article_title_locator = (By.XPATH, "//*[@resource-id='pcs']/android.view.View[1]/android.view.View[1]")
    bookmark_folder_locator = (By.XPATH,
                               "//*[@resource-id='org.wikipedia:id/recycler_view']//*[@class='android.view.ViewGroup'][1]")
    saved_bookmarks_button_locator = (By.XPATH,
                                      "//android.widget.FrameLayout[@content-desc='Saved']/android.widget.ImageView")
    back_arrow_locator = (By.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']")
    back_arrow_search_screen_locator = (By.XPATH,
                          "//*[@resource-id='org.wikipedia:id/search_toolbar']//*[@class='android.widget.ImageButton']")
    bookmark_button_locator = (By.ID, "org.wikipedia:id/article_menu_bookmark")

    def setup(self):
        self.driver = webdriver.Remote(APPIUM_ADDR, capabilities)
        # self.driver.implicitly_wait(5)
        self.click_skip_button_if_exists()

    def teardown(self):
        self.driver.orientation = "PORTRAIT"
        self.driver.quit()

    def click_to_search_result(self, search_result_number):
        search_result_object_locator = (By.XPATH, f"//*[@resource-id='org.wikipedia:id/search_results_list']//*[@class='android.view.ViewGroup'][{search_result_number}]")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(search_result_object_locator))
        search_result_object = self.driver.find_element(*search_result_object_locator)
        search_result_object.click()

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

    def click_back_arrow_on_search_screen(self):

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.back_arrow_search_screen_locator))
        back_arrow = self.driver.find_element(*self.back_arrow_search_screen_locator)
        back_arrow.click()

    def click_back_arrow_on_article_screen(self):

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.back_arrow_locator))
        back_arrow = self.driver.find_element(*self.back_arrow_locator)
        back_arrow.click()

    def click_add_article_to_bookmak_button(self):

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.bookmark_button_locator))
        bookmark_button = self.driver.find_element(*self.bookmark_button_locator)
        bookmark_button.click()

    def click_saved_bookmarks_button(self):

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.saved_bookmarks_button_locator))
        saved_bookmarks_button = self.driver.find_element(*self.saved_bookmarks_button_locator)
        saved_bookmarks_button.click()

    def click_on_bookmark_folder(self):

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.bookmark_folder_locator))
        bookmark_folder = self.driver.find_element(*self.bookmark_folder_locator)
        bookmark_folder.click()
        return bookmark_folder

    def swipe_left(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        element = self.driver.find_element(*locator)
        left_x = element.location['x']
        right_x = left_x + element.size['width']
        upper_y = element.location['y']
        lower_y = upper_y + element.size['height']
        middle_y = (upper_y + lower_y) / 2

        self.driver.swipe(right_x - 5, middle_y, left_x + 5, middle_y, 400)
        # action = TouchAction(self.driver)
        # action.press(x=right_x - 5, y=middle_y)
        # action.move_to(x=left_x + 5, y=middle_y)
        # action.release()
        # action.perform()

    def check_elements_amount(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator))
        elements = self.driver.find_elements(*locator)
        return len(elements)

    def get_article_title(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.article_title_locator))
        article_title_text = self.driver.find_element(*self.article_title_locator).text
        return article_title_text

    def assert_element_present(self):
        article_title_amount = len(self.driver.find_elements(*self.article_title_locator))
        if article_title_amount:
            check_result = "Article title is exist!"
        else:
            check_result = f"Article title is NOT found with locator: {self.article_title_locator}"
        return check_result

    def test_ex5(self):
        search_field = self.driver.find_element(*self.search_field_locator)
        search_field.click()
        search_field.send_keys('Java')
        for search_result_number in range(1, 3):
            self.click_to_search_result(search_result_number)
            self.click_add_article_to_bookmak_button()
            self.click_back_arrow_on_article_screen()
        self.click_back_arrow_on_search_screen()
        self.click_saved_bookmarks_button()
        self.click_on_bookmark_folder()

        articles_amount_before_delete = self.check_elements_amount(self.article_list_title_locator)
        self.swipe_left(self.article_list_title_locator)
        articles_amount_after_delete = self.check_elements_amount(self.article_list_title_locator)
        assert articles_amount_after_delete < articles_amount_before_delete
        last_article = self.driver.find_elements(*self.article_list_title_locator)[0]
        article_list_title_text = last_article.text
        last_article.click()
        article_title_text = self.get_article_title()
        assert article_title_text == article_list_title_text

    def test_ex6(self):
        search_field = self.driver.find_element(*self.search_field_locator)
        search_field.click()
        search_field.send_keys('Java')
        self.click_to_search_result(1)
        assert self.assert_element_present() is "Article title is exist!"

    def test_ex7(self):
        # def teardown(self):
        #     self.driver.orientation = "PORTRAIT"
        #     self.driver.quit()
        pass




