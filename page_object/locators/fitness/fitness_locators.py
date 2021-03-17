from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy


class FitnessLocators:
    def __init__(self, config):
        self.config = config

        self.VIEW_BY_THE_TIME_BUTTON = {
            "android": (By.XPATH, "//android.widget.TextView[contains(@text, 'View by time')]/.."),
            "ios": (MobileBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`label == 'View by time'`]"),
        }[self.config.platform_name]

        self.TIME_BUTTON = {
            "android": (By.XPATH, "//android.widget.TextView[contains(@text, 'Time')]/.."),
            "ios": (MobileBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`label == 'Time'`]"),
        }[self.config.platform_name]

        self.CREDITS_BUTTON = {
            "android": (By.XPATH, "//android.widget.TextView[contains(@text, 'Credits')]/.."),
            "ios": (MobileBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`label == 'Credits'`]"),
        }[self.config.platform_name]

        self.FAVORITES_BUTTON = {
            "android": (By.XPATH, "//android.widget.TextView[contains(@text, 'Favorites')]/.."),
            "ios": (MobileBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`label == 'Favorited'`]"),
        }[self.config.platform_name]

        self.AMENITIES_BUTTON = {
            "android": (By.XPATH, "//android.widget.TextView[contains(@text, 'Amenities')]/.."),
            "ios": (MobileBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`label == 'Amenities'`]"),
        }[self.config.platform_name]

        self.KEYWORD_SEARCH_BAR = {
            "android": (By.ID, "com.classpass.classpass.dev:id/searchBarText"),
            "ios": (MobileBy.ACCESSIBILITY_ID, "keywordSearchBar"),
        }[self.config.platform_name]
