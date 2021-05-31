from pages.main import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from lib.locators import ExploreLocator
from pages.left_menu_page import LeftMenuPage
import allure


class ExplorePage(BasePage):
    locator = ExploreLocator()

    def __init__(self, driver):
        super().__init__(driver)
        self.left_menu = LeftMenuPage(driver)

    @property
    def search_field(self):
        search_field = self.find_element(self.locator.get_locator('search_field'))
        return search_field

    def search_field_click(self):
        with allure.step("Клик ЛКМ по полю поиска"):
            search_field = self.search_field
        return search_field.click()

    def search_field_send_keys(self, keys):
        with allure.step(f"Ввод значения {keys} в поле поиска"):
            search_field = self.search_field
        return search_field.send_keys(keys)

    @property
    def search_button(self):
        search_field = self.find_element(self.locator.get_locator('search_button'))
        return search_field

    def search_button_click(self):
        with allure.step("Клик по кнопке поиска"):
            search_field = self.search_button
            return search_field.click()

    @property
    def close_button(self):
        close_button = self.find_element(self.locator.get_locator('close_search_button'))
        return close_button

    def results_number(self):
        try:
            search_results = WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located(self.locator.get_locator('search_results_list')))
            search_results_num = len(search_results)
            return search_results_num
        except TimeoutException:
            return 0

    @property
    def search_results(self):
        search_result = self.find_elements(self.locator.get_locator('search_result_object'))
        return search_result

    @property
    def back_arrow(self):
        back_arrow = self.find_element(self.locator.get_locator('back_arrow'))
        return back_arrow

    @property
    def cancel_search_button(self):
        cancel_search_button = self.find_element(self.locator.get_locator('cancel_search_button'))
        return cancel_search_button

    def cancel_search_button_click(self):
        with allure.step('Клик по кнопке отмены поиска'):
            cancel_search_button = self.cancel_search_button
        return cancel_search_button.click()

    @property
    def saved_button(self):
        saved_button = self.find_element(self.locator.get_locator('saved_button'))
        return saved_button

    def wait_for_element_by_title_and_description(self, title, description):
        locator = ExploreLocator()
        locator_with_replaced_title = self._replace_substring(
            locator.get_locator('element_by_title_and_description'),
            '{TITLE}',
            title)
        locator_with_replaced_title_end_description = self._replace_substring(
            locator_with_replaced_title,
            '{DESCRIPTION}',
            description)
        elements = self.find_element(
            locator_with_replaced_title_end_description)
        return elements

    @property
    def search_results_favorits(self):
        search_result = self.find_elements(self.locator.get_locator('search_results_favorits'))
        return search_result

    def article_add_to_favorits(self, search_result_id):
        with allure.step(f'Добавление статьи c id {search_result_id} в избранное'):
            search_result = self.find_elements(self.locator.get_locator('search_results_favorits'))
        return search_result[search_result_id].click()
