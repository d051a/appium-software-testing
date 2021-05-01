from pages.main import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class ArticleLocator:
    save_button = (By.ID, "org.wikipedia:id/article_menu_bookmark")
    back_arrow = (By.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']")
    article_title = (By.XPATH,
                             "//*[@resource-id='pcs']/android.view.View[1]/android.view.View[1]")


class ArticlePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def save_button(self):
        save_button = self.find_element(ArticleLocator.save_button)
        return save_button

    @property
    def back_arrow(self):
        back_arrow = self.find_element(ArticleLocator.back_arrow)
        return back_arrow

    @property
    def article_title(self):
        article_title = self.find_element(ArticleLocator.article_title)
        return article_title.text

    def assert_title_present(self):
        result = self.assert_element_present(ArticleLocator.article_title)
        if result:
            check_result = "Article title is exist!"
        else:
            check_result = f"Article title is NOT found with locator: {ArticleLocator.article_title}"
        return check_result


