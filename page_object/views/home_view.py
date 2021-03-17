from page_object.locators.home_locators import HomeLocators
from page_object.views.base_view import BaseView
from page_object.base_element import BaseElement


class Home(BaseView):
    def __init__(self, driver, config):
        super().__init__(driver, config)
        self.driver = driver
        self.config = config
        self.locators = HomeLocators(config=self.config)

    @property
    def welcome_label(self):
        self.wait_for(self.locators.WELCOME_LABEL, 10)
        return BaseElement(driver=self.driver, locator=self.locators.WELCOME_LABEL)

    @property
    def search_icon_tap_bar(self):
        self.wait_for(self.locators.WELCOME_LABEL, 10)
        return BaseElement(driver=self.driver, locator=self.locators.SEARCH_ICON_TAP_BAR)

    def open_search_screen(self):
        self.search_icon_tap_bar.click()
