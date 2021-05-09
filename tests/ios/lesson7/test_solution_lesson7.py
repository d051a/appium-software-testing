from pages.explore_page import ExplorePage
from pages.article_page import ArticlePage
from pages.saved_page import SavedPage
from pages.welcome_page import WelcomePage
import pytest


class TestLesson7:
    @pytest.fixture()
    def explore_screen(self, driver):
        return ExplorePage(driver)

    @pytest.fixture()
    def article_screen(self, driver):
        return ArticlePage(driver)

    @pytest.fixture()
    def saved_screen(self, driver):
        return SavedPage(driver)

    @pytest.fixture()
    def welcome_screen(self, driver):
        return WelcomePage(driver)

    def test_ex11(self, welcome_screen, explore_screen, article_screen, saved_screen):
        welcome_screen.click_on_skip_button()
        explore_screen.search_field.click()
        explore_screen.search_field.send_keys('Java')
        for search_result_number in range(0, 2):
            explore_screen.search_results[search_result_number].click()
            article_screen.save_button.click()
            article_screen.back_arrow.click()
        explore_screen.cancel_search_button.click()
        explore_screen.saved_button.click()
        saved_screen.bookmark_folders[0].click()

        saved_screen.sync_saved_articles_close_button.click()
        articles_amount_before_delete = saved_screen.get_articles_number()
        first_saved_article = saved_screen.saved_articles[0]
        saved_screen.swipe_left(first_saved_article)
        saved_screen.delete_button.click()
        articles_amount_after_delete = saved_screen.get_articles_number()
        assert articles_amount_after_delete < articles_amount_before_delete
        last_article = saved_screen.saved_articles[0]
        article_list_title_text = last_article.text
        last_article.click()
        assert article_screen.get_article_title_by_search_result_title(article_list_title_text) == article_list_title_text

    def test_ex12(self, welcome_screen, explore_screen):
        search_text = 'JavaScript'
        welcome_screen.click_on_skip_button()
        explore_screen.search_field.click()
        explore_screen.search_field.send_keys(search_text)
        explore_screen.wait_for_element_by_title_and_description(
            'JavaScript', 'High-level programming language')
        explore_screen.wait_for_element_by_title_and_description(
            'JavaScript syntax', 'Rule set defining a correctly structured JavaScript program')
        explore_screen.wait_for_element_by_title_and_description(
            'JavaScript engine', 'Implementation of JavaScript')
