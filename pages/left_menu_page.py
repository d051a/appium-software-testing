from pages.main import BasePage
from lib.locators import LeftMenuLocator
from config import APP_USER, APP_PASSWORD


class LeftMenuPage(BasePage):
    locator = LeftMenuLocator()

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def left_menu_button(self):
        left_menu_button = self.find_element(
            self.locator.get_locator('left_menu_button'))
        return left_menu_button

    @property
    def left_menu_login_button(self):
        left_menu_login_button = self.find_element(
            self.locator.get_locator('left_menu_login_button'))
        return left_menu_login_button

    @property
    def login_field(self):
        login_input = self.find_element(
            self.locator.get_locator('login_field'))
        return login_input

    @property
    def password_field(self):
        login_input = self.find_element(
            self.locator.get_locator('password_field'))
        return login_input

    @property
    def login_button(self):
        login_button = self.find_element(
            self.locator.get_locator('login_button'))
        return login_button

    @property
    def left_menu_watchlist_button(self):
        left_menu_watchlist_button = self.find_element(
            self.locator.get_locator('left_menu_watchlist_button'))
        return left_menu_watchlist_button

    def check_notifications_exist(self):
        notification_icon = self.locator.get_locator('notificaton_icon')
        if self.driver.find_elements(*notification_icon):
            return True
        else:
            return False

    def auth_if_not_login(self):
        if not self.check_notifications_exist():
            self.left_menu_button.click()
            self.left_menu_login_button.click()
            self.login_field.send_keys(APP_USER)
            self.password_field.send_keys(APP_PASSWORD)
            self.login_button.click()

    def open_watchlist(self):
        self.left_menu_button.click()
        self.left_menu_watchlist_button.click()




