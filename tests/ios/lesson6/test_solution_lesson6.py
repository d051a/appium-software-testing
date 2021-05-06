from pages.welcome_page import WelcomePage
import pytest
import time


class TestLesson6:
    @pytest.fixture()
    def welcome_screen(self, driver):
        return WelcomePage(driver)

    def test_ex10(self, welcome_screen):
        pass

