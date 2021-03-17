from page_object.locators.fitness.fitness_locators import FitnessLocators
from page_object.views.base_view import BaseView
from page_object.base_element import BaseElement


class Fitness(BaseView):
    def __init__(self, driver, config):
        super().__init__(driver, config)
        self.driver = driver
        self.config = config
        self.locators = FitnessLocators(config=self.config)

    @property
    def view_by_the_time_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.VIEW_BY_THE_TIME_BUTTON)

    @property
    def time_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.TIME_BUTTON)

    @property
    def credits_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.CREDITS_BUTTON)

    @property
    def favorites_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.FAVORITES_BUTTON)

    @property
    def amenities_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.AMENITIES_BUTTON)

    @property
    def keyword_search_bar(self):
        return BaseElement(driver=self.driver, locator=self.locators.KEYWORD_SEARCH_BAR)

    def view_by_the_time_button_visibility(self):
        locators = FitnessLocators(config=self.config)
        return self.wait_for(locators.VIEW_BY_THE_TIME_BUTTON)

    def time_button_visibility(self):
        locators = FitnessLocators(config=self.config)
        return self.wait_for(locators.TIME_BUTTON)

    def credits_button_visibility(self):
        locators = FitnessLocators(config=self.config)
        return self.wait_for(locators.CREDITS_BUTTON)

    def favorites_button_visibility(self):
        locators = FitnessLocators(config=self.config)
        return self.wait_for(locators.FAVORITES_BUTTON)

    def amenities_button_visibility(self):
        locators = FitnessLocators(config=self.config)
        return self.wait_for(locators.AMENITIES_BUTTON)

    def swipe_left_from_time_button(self):
        self.swipe_left_from(self.time_button)
