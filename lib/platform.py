import os
from appium import webdriver
from capabilities import capabilities


class Platform:
    PLATFORM_IOS = 'ios'
    PLATFORM_ANDROID = 'android'
    APPIUM_URL = 'http://localhost:4723/wd/hub'

    def get_driver(self):
        desired_capabilities = self.get_capabilities()
        driver = webdriver.Remote(self.APPIUM_URL, desired_capabilities)
        return driver

    @staticmethod
    def get_platform():
        return os.environ.get('PLATFORM')

    def is_platform(self, my_platform):
        return self.get_platform() == my_platform

    def is_android(self):
        return self.is_platform(self.PLATFORM_ANDROID)

    def is_ios(self):
        return self.is_platform(self.PLATFORM_IOS)

    def get_capabilities(self):
        platform = self.get_platform()
        if platform == self.PLATFORM_IOS:
            return capabilities[self.PLATFORM_IOS]
        elif platform == self.PLATFORM_ANDROID:
            return capabilities[self.PLATFORM_ANDROID]
        else:
            raise Exception(f"Environment parameter 'PLATFORM' not set "
                            f"or is not equal to '{self.PLATFORM_IOS}'"
                            f" or '{self.PLATFORM_ANDROID}'")
