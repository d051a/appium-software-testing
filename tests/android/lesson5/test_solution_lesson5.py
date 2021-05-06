from pages.explore_page import ExplorePage
from pages.article_page import ArticlePage
from pages.saved_page import SavedPage
import pytest


class TestLesson5:
    @pytest.fixture()
    def explore_screen(self, driver):
        return ExplorePage(driver)

    @pytest.fixture()
    def article_screen(self, driver):
        return ArticlePage(driver)

    @pytest.fixture()
    def saved_screen(self, driver):
        return SavedPage(driver)

    def test_ref_ex3(self, explore_screen):
        explore_screen.search_field.send_keys('appium')
        assert explore_screen.results_number() > 1
        explore_screen.close_button.click()
        assert explore_screen.results_number() == 0

    def test_ref_ex5(self, explore_screen, article_screen, saved_screen):
        explore_screen.search_field.send_keys('Java')
        for search_result_number in range(1, 3):
            explore_screen.search_results[search_result_number].click()
            article_screen.save_button.click()
            article_screen.back_arrow.click()
        explore_screen.back_arrow.click()
        explore_screen.saved_button.click()
        saved_screen.bookmark_folders[0].click()

        articles_amount_before_delete = saved_screen.get_articles_number()
        first_saved_article = saved_screen.saved_articles[0]
        saved_screen.swipe_left(first_saved_article)
        articles_amount_after_delete = saved_screen.get_articles_number()
        assert articles_amount_after_delete < articles_amount_before_delete
        last_article = saved_screen.saved_articles[0]
        article_list_title_text = last_article.text
        last_article.click()
        assert article_screen.article_title == article_list_title_text

    def test_ref_ex6(self, explore_screen, article_screen):
        explore_screen.search_field.send_keys('Java')
        explore_screen.search_results[0].click()
        assert article_screen.assert_title_present() is "Article title is exist!"

    def test_ex9(self, explore_screen):
        search_text = 'JavaScript'
        explore_screen.search_field.send_keys(search_text)
        articles_with_text_in_title_and_description = explore_screen.\
            wait_for_element_by_title_and_description('JavaScript',
                                                      'High-level')
        all_find_articles = explore_screen.search_results
        print('articles_with_text_in_title_and_description', articles_with_text_in_title_and_description)
        print('all_find_articles: - ', all_find_articles)

        for num, article in enumerate(articles_with_text_in_title_and_description):
            for element in all_find_articles:
                if article == element:
                    print("DONE!", )
                else:
                    print("NO!", type(element), type(article))
            # assert article == all_find_articles[num]


# //android.view.ViewGroup[(./android.widget.TextView[(@resource-id='org.wikipedia:id/page_list_item_title' and contains(@text, 'JavaScript'))]) and (./android.widget.TextView[(@resource-id='org.wikipedia:id/page_list_item_description' and contains(@text, 'High-level'))])]