from pages.main import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class SavedLocator:
    bookmark_folder = (By.XPATH,
                               "//*[@resource-id='org.wikipedia:id/recycler_view']//*[@class='android.view.ViewGroup']")
    articles_titles_list = (By.XPATH,
                            "//android.widget.TextView[contains(@resource-id, 'org.wikipedia:id/page_list_item_title')]")


class SavedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def bookmark_folders(self):
        bookmark_folders = self.find_elements(SavedLocator.bookmark_folder)
        return bookmark_folders

    def get_articles_number(self):
        articles_number = self.check_elements_amount(SavedLocator.articles_titles_list)
        return articles_number

    @property
    def saved_articles(self):
        saved_articles = self.find_elements(SavedLocator.articles_titles_list)
        return saved_articles

    def swipe_left(self, element):
        left_x = element.location['x']
        right_x = left_x + element.size['width']
        upper_y = element.location['y']
        lower_y = upper_y + element.size['height']
        middle_y = (upper_y + lower_y) / 2
        self.driver.swipe(right_x - 5, middle_y, left_x + 5, middle_y, 400)
