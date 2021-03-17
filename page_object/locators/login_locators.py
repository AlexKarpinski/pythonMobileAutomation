from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy


class LoginLocators:
    def __init__(self, config):
        self.config = config

        self.LOGIN_BUTTON = {
            "android": (MobileBy.ACCESSIBILITY_ID, "Log in with account"),
            "ios": (By.XPATH, "//XCUIElementTypeButton[@name='Log in with account']"),
        }[self.config.platform_name]

        self.EMAIL_FIELD = {
            "android": (By.XPATH, "//android.widget.EditText[contains(@text, 'Email address')]"),
            "ios": (By.XPATH, "(//XCUIElementTypeOther[@name='Email address'])[2]"),
        }[self.config.platform_name]

        self.PASSWORD_FIELD = {
            "android": (By.XPATH, "//android.widget.EditText[contains(@text, 'Password')]"),
            "ios": (By.XPATH, "(//XCUIElementTypeOther[@name='Password'])[2]"),
        }[self.config.platform_name]

        self.LOG_IN_BUTTON = {
            "android": (By.XPATH, "(//android.widget.TextView[contains(@text, 'Log in')])[2]/.."),
            "ios": (By.XPATH, "//XCUIElementTypeButton[@name='Log in']"),
        }[self.config.platform_name]

        self.UNSUCCESSFUL_LOGIN_MESSAGE = {
            "android": (By.XPATH, "//android.widget.TextView[contains(@text, 'The password or email')]"),
            "ios": (MobileBy.NAME, "The password or email address you entered is incorrect. Reset your password or "
                                   "contact us if youʼre having trouble logging in."),
        }[self.config.platform_name]

        self.BACK_BUTTON = {
            "android": (MobileBy.ACCESSIBILITY_ID, "Navigate up"),
            "ios": (MobileBy.ACCESSIBILITY_ID, "Back"),
        }[self.config.platform_name]
