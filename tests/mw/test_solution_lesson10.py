from pages.explore_page import ExplorePage
from pages.article_page import ArticlePage
from pages.saved_page import SavedPage
from pages.welcome_page import WelcomePage
import pytest
import time
import allure
from config import APP_URL


@allure.epic('Тесты для статей')
class TestLesson10:
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

    @allure.title('TEST: Добавление статей в избранное, удаление и проверка названия')
    @allure.feature('Search', 'Articles', 'Favorites')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_ex20(self, welcome_screen, explore_screen, article_screen, saved_screen):
        explore_screen.open_page(APP_URL)
        explore_screen.left_menu.auth_if_not_login()
        explore_screen.search_button_click()
        explore_screen.search_field_click()
        explore_screen.search_field_send_keys('Windows')
        for search_result_number in range(0, 2):
            explore_screen.article_add_to_favorits(search_result_number)
        explore_screen.cancel_search_button_click()
        explore_screen.left_menu.open_watchlist()
        articles_amount_before_delete = saved_screen.get_favorits_number()
        saved_screen.article_favotirs_remove(0)
        time.sleep(2)
        articles_amount_after_delete = saved_screen.get_favorits_number()
        assert articles_amount_after_delete < articles_amount_before_delete
        saved_screen_article_title = saved_screen.saved_article_title(-1)
        saved_screen.saved_article_click(-1)
        assert article_screen.article_title == saved_screen_article_title
