from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy


class HomeLocators:
    def __init__(self, config):
        self.config = config

        self.WELCOME_LABEL = {
            "android": (By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to ClassPass')]"),
            "ios": (By.XPATH, "//XCUIElementTypeButton[@name='Welcome to ClassPass']"),
        }[self.config.platform_name]

        self.SEARCH_ICON_TAP_BAR = {
            "android": (By.XPATH, "//android.widget.FrameLayout[@content-desc='Search']"),
            "ios": (By.XPATH, "//XCUIElementTypeButton[@name='Search']"),
        }[self.config.platform_name]
