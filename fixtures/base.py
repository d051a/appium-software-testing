import pytest
from config import APPIUM_ADDR
from capabilities import capabilities
from appium import webdriver


@pytest.fixture(scope='function')
def driver():
    capabilities['orientation'] = 'PORTRAIT'
    driver = webdriver.Remote(APPIUM_ADDR, capabilities)
    yield driver
    driver.quit()


