import pytest
from lib.platform import Platform


@pytest.fixture(scope='function')
def driver():
    platform = Platform()
    driver = platform.get_driver()
    yield driver
    driver.quit()


