from pages.main import BasePage
from lib.locators import ArticleLocator
import os


class ArticlePage(BasePage):
    locator = ArticleLocator()

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def save_button(self):
        save_button = self.find_element(self.locator.get_locator('save_button'))
        return save_button

    @property
    def back_arrow(self):
        back_arrow = self.find_element(self.locator.get_locator('back_arrow'))
        return back_arrow

    @property
    def article_title(self, title=None):
        article_title = self.find_element(self.locator.get_locator('article_title'))
        return article_title.text

    def get_article_title_by_search_result_title(self, title):
        locator_with_replaced_title = self._replace_substring(
            self.locator.get_locator('article_title'),
            '{TITLE}',
            title)
        article_title = self.find_element(locator_with_replaced_title)
        return article_title.text


    def assert_title_present(self):
        locator = self.locator.get_locator('article_title')
        result = self.assert_element_present(locator)
        if result:
            check_result = "Article title is exist!"
        else:
            check_result = f"Article title is NOT found with locator: {locator}"
        return check_result


