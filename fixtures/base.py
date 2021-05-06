import pytest
import capabilities
from config import APPIUM_ADDR
from appium import webdriver


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Remote(APPIUM_ADDR, capabilities.get_capabilities())
    yield driver
    driver.quit()


