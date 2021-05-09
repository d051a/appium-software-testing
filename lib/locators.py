import os
from selenium.webdriver.common.by import By


class Locator:
    PLATFORM_IOS = 'ios'
    PLATFORM_ANDROID = 'android'

    locators = {'android': {},
                'ios': {},
                }

    def get_locator(self, locator_name):
        platform = self.get_platform()
        if platform == self.PLATFORM_IOS:
            return self.__class__.locators[self.PLATFORM_IOS][locator_name]
        elif platform == self.PLATFORM_ANDROID:
            return self.__class__.locators[self.PLATFORM_ANDROID][locator_name]
        else:
            raise Exception(f"Environment parameter 'PLATFORM' not set "
                            f"or is not equal to '{self.PLATFORM_IOS}'"
                            f" or '{self.PLATFORM_ANDROID}'")

    @staticmethod
    def get_platform():
        return os.environ.get('PLATFORM')

    def is_platform(self, my_platform):
        return self.get_platform() == my_platform

    def is_android(self):
        return self.is_platform(self.PLATFORM_ANDROID)

    def is_ios(self):
        return self.is_platform(self.PLATFORM_IOS)


class ExploreLocator(Locator):
    locators = {'android':
                    {'search_field': (By.ID, "org.wikipedia:id/search_container"),
                     'search_result_object': (By.XPATH, "//*[@resource-id='org.wikipedia:id/search_results_list']//*[@class='android.view.ViewGroup']"),
                     'close_search_button': (By.ID, "org.wikipedia:id/search_close_btn"),
                     'search_results_list': (By.ID, "org.wikipedia:id/page_list_item_title"),
                     'back_arrow': (By.XPATH, "//*[@resource-id='org.wikipedia:id/search_toolbar']//*[@class='android.widget.ImageButton']"),
                     'saved_button': (By.XPATH, "//android.widget.FrameLayout[@content-desc='Saved']/android.widget.ImageView"),
                     'element_by_title_and_description': (By.XPATH, "//android.view.ViewGroup[(./android.widget.TextView[(@resource-id='org.wikipedia:id/page_list_item_title' and contains(@text, '{TITLE}'))]) and (./android.widget.TextView[(@resource-id='org.wikipedia:id/page_list_item_description' and contains(@text, '{DESCRIPTION}'))])]"),

                     },
                'ios':
                    {'search_field': (By.XPATH, "//XCUIElementTypeSearchField[@name='Search Wikipedia']"),
                     'search_result_object': (By.XPATH,
                                              "//*[@type='XCUIElementTypeCell']"),
                     'close_search_button': (By.ID, ""),
                     'search_results_list': (By.ID, ""),
                     'cancel_search_button': (By.XPATH, "//XCUIElementTypeStaticText[@name='Cancel']"),
                     'saved_button': (By.XPATH, "//XCUIElementTypeButton[@name='Saved']"),
                     'element_by_title_and_description': (By.XPATH, "//XCUIElementTypeOther[(./XCUIElementTypeStaticText[@name='{TITLE}']) and (./XCUIElementTypeStaticText[@name='{DESCRIPTION}'])]"),
                     },
                }


class WelcomeLocator(Locator):
    locators = {'android':
                    {'skip_button': (By.ID, "org.wikipedia:id/fragment_onboarding_skip_button"),
                     'next_button': (By.XPATH, ""),
                     },
                'ios':
                    {'skip_button': (By.XPATH,
                                     "//XCUIElementTypeStaticText[@name='Skip']"),
                     'next_button': (By.XPATH,
                                     "//XCUIElementTypeStaticText[@name='Next']"),
                     },
                }


class ArticleLocator(Locator):
    locators = {'android':
                    {'save_button': (By.ID, "org.wikipedia:id/article_menu_bookmark"),
                     'back_arrow': (By.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']"),
                     'article_title': (By.XPATH, "//*[@resource-id='pcs']/android.view.View[1]/android.view.View[1]"),
                     },
                'ios':
                    {'save_button': (By.XPATH, "//XCUIElementTypeButton[@name='Save for later']"),
                     'back_arrow': (By.XPATH, "//XCUIElementTypeButton[@name='Back']"),
                     'article_title': (By.ID, "{TITLE}"),
                     },
                }


class SavedLocator(Locator):
    locators = {'android':
                    {'bookmark_folder': (By.XPATH, "//*[@resource-id='org.wikipedia:id/recycler_view']//*[@class='android.view.ViewGroup']"),
                     'articles_titles_list': (By.XPATH, "//android.widget.TextView[contains(@resource-id, 'org.wikipedia:id/page_list_item_title')]"),
                     },
                'ios':
                    {'bookmark_folder': (By.XPATH,
                                     "//XCUIElementTypeButton[@name='Saved']"),
                     'articles_titles_list': (By.XPATH, "//XCUIElementTypeCollectionView//XCUIElementTypeCell//XCUIElementTypeOther//XCUIElementTypeStaticText[1]"),
                     'sync_saved_articles_close_button': (By.XPATH, "//XCUIElementTypeButton[@name='Close']"),
                     'delete_button': (By.XPATH, "//XCUIElementTypeButton[@name='swipe action delete']"),
                     },
                }
