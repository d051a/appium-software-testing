import pytest
import capabilities
from config import APPIUM_ADDR
from appium import webdriver
from lib.platform import Platform


@pytest.fixture(scope='function')
def driver():
    platform = Platform()
    driver = platform.get_driver()
    yield driver
    driver.quit()


