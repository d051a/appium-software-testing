from pages.main import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class ExploreLocator:
    search_field = (By.ID, "org.wikipedia:id/search_container")
    search_field_ios = (By.ID, "org.wikipedia:id/search_container")
    close_search_button = (By.ID, "org.wikipedia:id/search_close_btn")
    search_results_list = (By.ID, "org.wikipedia:id/page_list_item_title")
    search_result_object = (By.XPATH, "//*[@resource-id='org.wikipedia:id/search_results_list']//*[@class='android.view.ViewGroup']")
    back_arrow = (By.XPATH, "//*[@resource-id='org.wikipedia:id/search_toolbar']//*[@class='android.widget.ImageButton']")
    saved_button = (By.XPATH, "//android.widget.FrameLayout[@content-desc='Saved']/android.widget.ImageView")
    element_by_title_and_description = (By.XPATH, "//android.view.ViewGroup[(./android.widget.TextView[(@resource-id='org.wikipedia:id/page_list_item_title' and contains(@text, '{TITLE}'))]) and (./android.widget.TextView[(@resource-id='org.wikipedia:id/page_list_item_description' and contains(@text, '{DESCRIPTION}'))])]")


class ExplorePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def search_field(self):
        search_field = self.find_element(ExploreLocator.search_field)
        return search_field

    @property
    def close_button(self):
        close_button = self.find_element(ExploreLocator.close_search_button)
        return close_button

    def results_number(self):
        try:
            search_results = WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located(ExploreLocator.search_results_list))
            search_results_num = len(search_results)
            return search_results_num
        except TimeoutException:
            return 0

    @property
    def search_results(self):
        search_result = self.find_elements(ExploreLocator.search_result_object)
        return search_result

    @property
    def back_arrow(self):
        back_arrow = self.find_element(ExploreLocator.back_arrow)
        return back_arrow

    @property
    def saved_button(self):
        saved_button = self.find_element(ExploreLocator.saved_button)
        return saved_button

    def wait_for_element_by_title_and_description(self, title, description):
        locator_with_replaced_title = self._replace_substring(
            ExploreLocator.element_by_title_and_description,
            '{TITLE}',
            title)
        locator_with_replaced_title_end_description = self._replace_substring(
            locator_with_replaced_title,
            '{DESCRIPTION}',
            description)
        elements = self.find_elements(
            locator_with_replaced_title_end_description)
        return elements
