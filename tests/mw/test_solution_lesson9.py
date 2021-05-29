from pages.explore_page import ExplorePage
from pages.article_page import ArticlePage
from pages.saved_page import SavedPage
from pages.welcome_page import WelcomePage
import pytest
import time
from config import APP_URL


class TestLesson9:
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

    def test_ex17(self, welcome_screen, explore_screen, article_screen, saved_screen):
        explore_screen.open_page(APP_URL)
        explore_screen.left_menu.auth_if_not_login()
        explore_screen.search_button.click()
        explore_screen.search_field.click()
        explore_screen.search_field.send_keys('Windows')
        for search_result_number in range(0, 2):
            explore_screen.search_results_favorits[search_result_number].click()
        explore_screen.cancel_search_button.click()
        explore_screen.left_menu.open_watchlist()
        articles_amount_before_delete = saved_screen.get_favorits_number()
        saved_screen.article_favotirs_marks[0].click()
        time.sleep(2)
        articles_amount_after_delete = saved_screen.get_favorits_number()
        assert articles_amount_after_delete < articles_amount_before_delete

        last_article = saved_screen.saved_articles[-1]
        article_list_title_text = last_article.text
        last_article.click()
        assert article_screen.article_title == article_list_title_text
