import os
from selenium.webdriver.common.by import By
from config import PLATFORM_IOS, PLATFORM_ANDROID, PLATFORM_MW


class Locator:

    locators = {PLATFORM_ANDROID: {},
                PLATFORM_IOS: {},
                PLATFORM_MW: {},
                }

    def get_locator(self, locator_name):
        platform = self.get_platform()
        if platform == PLATFORM_IOS:
            return self.__class__.locators[PLATFORM_IOS][locator_name]
        elif platform == PLATFORM_ANDROID:
            return self.__class__.locators[PLATFORM_ANDROID][locator_name]
        elif platform == PLATFORM_MW:
            return self.__class__.locators[PLATFORM_MW][locator_name]
        else:
            raise Exception(f"Environment parameter 'PLATFORM' not set "
                            f"or is not equal to '{PLATFORM_IOS}'"
                            f" or '{PLATFORM_ANDROID}'")

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


class LeftMenuLocator(Locator):
    locators = {PLATFORM_MW:
                    {'left_menu_button': (By.ID, "mw-mf-main-menu-button"),
                     'notificaton_icon': (
                         By.ID, "user-notifications"),
                     'left_menu_login_button': (
                         By.CSS_SELECTOR, ".menu__item--login > span"),
                     'left_menu_watchlist_button': (
                         By.XPATH, "//*[@data-event-name='menu.unStar']"),
                     'login_field': (By.ID, "wpName1"),
                     'password_field': (By.ID, "wpPassword1"),
                     'login_button': (By.ID, "wpLoginAttempt"),
                     },
                }


class ExploreLocator(Locator):
    locators = {PLATFORM_ANDROID:
                    {'search_field': (By.ID, "org.wikipedia:id/search_container"),
                     'search_result_object': (By.XPATH, "//*[@resource-id='org.wikipedia:id/search_results_list']//*[@class='android.view.ViewGroup']"),
                     'close_search_button': (By.ID, "org.wikipedia:id/search_close_btn"),
                     'search_results_list': (By.ID, "org.wikipedia:id/page_list_item_title"),
                     'back_arrow': (By.XPATH, "//*[@resource-id='org.wikipedia:id/search_toolbar']//*[@class='android.widget.ImageButton']"),
                     'saved_button': (By.XPATH, "//android.widget.FrameLayout[@content-desc='Saved']/android.widget.ImageView"),
                     'element_by_title_and_description': (By.XPATH, "//android.view.ViewGroup[(./android.widget.TextView[(@resource-id='org.wikipedia:id/page_list_item_title' and contains(@text, '{TITLE}'))]) and (./android.widget.TextView[(@resource-id='org.wikipedia:id/page_list_item_description' and contains(@text, '{DESCRIPTION}'))])]"),

                     },
                PLATFORM_IOS:
                    {'search_field': (By.XPATH, "//XCUIElementTypeSearchField[@name='Search Wikipedia']"),
                     'search_result_object': (By.XPATH,
                                              "//*[@type='XCUIElementTypeCell']"),
                     'close_search_button': (By.ID, ""),
                     'search_results_list': (By.ID, ""),
                     'cancel_search_button': (By.XPATH, "//XCUIElementTypeStaticText[@name='Cancel']"),
                     'saved_button': (By.XPATH, "//XCUIElementTypeButton[@name='Saved']"),
                     'element_by_title_and_description': (By.XPATH, "//XCUIElementTypeOther[(./XCUIElementTypeStaticText[@name='{TITLE}']) and (./XCUIElementTypeStaticText[@name='{DESCRIPTION}'])]"),
                     },
                PLATFORM_MW:
                    {'search_field': (By.CSS_SELECTOR, ".search:nth-child(1)"),
                     'search_button': (By.XPATH, "//button[@id='searchIcon']"),
                     'search_result_object': (
                     By.XPATH, "//div[@class='results']//li"),
                     'search_results_favorits': (By.XPATH,
                                                 "//*[contains(@class, 'mw-ui-icon-wikimedia-star-base20')]"),
                     'next_button': (By.XPATH, ""),
                     'cancel_search_button': (By.XPATH,
                                              "//div[@class='header-action']//button[contains(@class, 'mw-ui-icon-element')]"),
                     },
                }


class WelcomeLocator(Locator):
    locators = {PLATFORM_ANDROID:
                    {'skip_button': (By.ID, "org.wikipedia:id/fragment_onboarding_skip_button"),
                     'next_button': (By.XPATH, ""),
                     },
                PLATFORM_IOS:
                    {'skip_button': (By.XPATH,
                                     "//XCUIElementTypeStaticText[@name='Skip']"),
                     'next_button': (By.XPATH,
                                     "//XCUIElementTypeStaticText[@name='Next']"),
                     },
                }


class ArticleLocator(Locator):
    locators = {PLATFORM_ANDROID:
                    {'save_button': (By.ID, "org.wikipedia:id/article_menu_bookmark"),
                     'back_arrow': (By.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']"),
                     'article_title': (By.XPATH, "//*[@resource-id='pcs']/android.view.View[1]/android.view.View[1]"),
                     },
                PLATFORM_IOS:
                    {'save_button': (By.XPATH, "//XCUIElementTypeButton[@name='Save for later']"),
                     'back_arrow': (By.XPATH, "//XCUIElementTypeButton[@name='Back']"),
                     'article_title': (By.ID, "{TITLE}"),
                     },
                PLATFORM_MW:
                    {'save_button': (By.ID, "ca-watch"),
                     'back_arrow': (By.XPATH, ""),
                     'article_title': (By.XPATH, "//div[@class='page-heading']//h1"),
                     },
                }


class SavedLocator(Locator):
    locators = {PLATFORM_ANDROID:
                    {'bookmark_folder': (By.XPATH, "//*[@resource-id='org.wikipedia:id/recycler_view']//*[@class='android.view.ViewGroup']"),
                     'articles_titles_list': (By.XPATH, "//android.widget.TextView[contains(@resource-id, 'org.wikipedia:id/page_list_item_title')]"),
                     },
                PLATFORM_IOS:
                    {'bookmark_folder': (By.XPATH,
                                     "//XCUIElementTypeButton[@name='Saved']"),
                     'articles_titles_list': (By.XPATH, "//XCUIElementTypeCollectionView//XCUIElementTypeCell//XCUIElementTypeOther//XCUIElementTypeStaticText[1]"),
                     'sync_saved_articles_close_button': (By.XPATH, "//XCUIElementTypeButton[@name='Close']"),
                     'delete_button': (By.XPATH, "//XCUIElementTypeButton[@name='swipe action delete']"),
                     },
                PLATFORM_MW:
                    {'bookmark_folder': (By.XPATH, ""),
                     'articles_titles_list': (By.XPATH, "//li[@class='page-summary with-watchstar']//h3"),
                     'article_favotirs_unmark': (By.XPATH,
                                                 "//*[contains(@class, 'mw-ui-icon-wikimedia-star-base20')]"),
                     'article_favotirs_mark': (By.XPATH,
                                                 "//*[contains(@class, 'mw-ui-icon mw-ui-icon-wikimedia-unStar-progressive')]"),
                     },
                }
