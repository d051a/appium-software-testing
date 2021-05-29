import os


capabilities = {
    'android': {
        "platformName": "Android",
        "deviceName": "AndroidTestDevice",
        "platformVersion": "8.0",
        "appPackage": "org.wikipedia",
        "appActivity": ".main.MainActivity",
        "orientation": "PORTRAIT",
    },
    'ios': {
        "platformName": "iOS",
        "deviceName": "iPhone 8",
        "orientation": "PORTRAIT",
        "platformVersion": "13.5",
        "app": "/Users/d051a/Desktop/LEARN/APPIUM/apps/Wikipedia.app",
        "LOCALE": "en",
        "LANGAUGE": "en",
        "sendKeyStrategy": "setValue"
    },
    'mw': {
        "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
    },
}


def get_capabilities():
    platform = get_platform()
    if platform == 'ios':
        return capabilities['ios']
    elif platform == 'android':
        return capabilities['android']
    elif platform is None:
        print("Environment parameter 'PLATFORM' not set")


def get_platform():
    platform = os.environ.get('PLATFORM')
    if platform == 'ios':
        return 'ios'
    elif platform == 'android':
        return 'android'
