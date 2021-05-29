import os
from appium import webdriver
from capabilities import capabilities
from selenium import webdriver as selenium_driver
from config import APPIUM_ADDR, PLATFORM_IOS, PLATFORM_ANDROID, PLATFORM_MW


class Platform:
    def get_driver(self):
        desired_capabilities = self.get_capabilities()
        platform = self.get_platform()
        if platform == PLATFORM_MW:
            chrome_options = selenium_driver.ChromeOptions()
            chrome_options.add_experimental_option("mobileEmulation",
                                                   desired_capabilities)
            driver = selenium_driver.Chrome(options=chrome_options)
            return driver
        else:
            driver = webdriver.Remote(APPIUM_ADDR, desired_capabilities)
            return driver

    @staticmethod
    def get_platform():
        return os.environ.get('PLATFORM')

    def is_platform(self, my_platform):
        return self.get_platform() == my_platform

    def is_android(self):
        return self.is_platform(PLATFORM_ANDROID)

    def is_ios(self):
        return self.is_platform(PLATFORM_IOS)

    def is_mw(self):
        return self.is_platform(PLATFORM_MW)

    def get_capabilities(self):
        platform = self.get_platform()
        if platform == PLATFORM_IOS:
            return capabilities[PLATFORM_IOS]
        elif platform == PLATFORM_ANDROID:
            return capabilities[PLATFORM_ANDROID]
        elif platform == PLATFORM_MW:
            return capabilities[PLATFORM_MW]
        else:
            raise Exception(f"Environment parameter 'PLATFORM' not set "
                            f"or is not equal to '{PLATFORM_IOS}'"
                            f" or '{PLATFORM_ANDROID}'")
