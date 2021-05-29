from pages.main import BasePage
from lib.locators import SavedLocator


class SavedPage(BasePage):
    locator = SavedLocator()

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def bookmark_folders(self):
        bookmark_folders = self.find_elements(self.locator.get_locator('bookmark_folder'))
        return bookmark_folders

    @property
    def saved_articles(self):
        saved_articles = self.find_elements(self.locator.get_locator('articles_titles_list'))
        return saved_articles

    @property
    def sync_saved_articles_close_button(self):
        close_button = self.find_element(self.locator.get_locator('sync_saved_articles_close_button'))
        return close_button

    @property
    def delete_button(self):
        delete_button = self.find_element(self.locator.get_locator('delete_button'))
        return delete_button

    @property
    def article_favotirs_marks(self):
        article_favotirs_mark = self.find_elements(self.locator.get_locator('article_favotirs_mark'))
        return article_favotirs_mark

    def get_favorits_number(self):
        favorits_mark_number = self.check_elements_amount(self.locator.get_locator('article_favotirs_mark'))
        return favorits_mark_number

    def get_articles_number(self):
        articles_number = self.check_elements_amount(self.locator.get_locator('articles_titles_list'))
        return articles_number

    def swipe_left(self, element):
        left_x = element.location['x']
        right_x = left_x + element.size['width']
        upper_y = element.location['y']
        lower_y = upper_y + element.size['height']
        middle_y = (upper_y + lower_y) / 2
        self.driver.swipe(right_x - 5, middle_y, left_x + 5, middle_y, 400)


