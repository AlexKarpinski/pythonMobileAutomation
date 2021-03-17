from page_object.locators.profile_locators import ProfileLocators
from page_object.views.base_view import BaseView
from page_object.base_element import BaseElement


class Profile(BaseView):
    def __init__(self, driver, config):
        super().__init__(driver, config)
        self.driver = driver
        self.config = config
        self.locators = ProfileLocators(config=self.config)

    @property
    def profile_icon(self):
        return BaseElement(driver=self.driver, locator=self.locators.PROFILE_ICON)

    @property
    def settings_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.SETTINGS_BUTTON)

    @property
    def log_out_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.LOG_OUT_BUTTON)

    @property
    def support_label(self):
        return BaseElement(driver=self.driver, locator=self.locators.SUPPORT_LABEL)

    def log_out(self):
        self.profile_icon.click()
        self.settings_button.click()
        self.scroll_up_from(self.support_label)
        self.log_out_button.click()
