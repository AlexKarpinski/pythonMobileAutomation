import allure
import pytest

from page_object.views.fitness.fitness_view import Fitness
from page_object.views.fitness.navigation_view import Navigation
from page_object.views.login_view import Login
from page_object.views.profile_view import Profile
from page_object.data.constants import Constants
from page_object.views.home_view import Home
from page_object.views.search_view import Search


class TestSearchView:

    @pytest.fixture(scope="class")
    def search_view(self, driver, config, env_config):
        # Log out
        # if config.platform_name == "ios":
        #    profile = Profile(driver=driver, config=config)
        #    profile.log_out()

        # Log in
        login = Login(driver=driver, config=config)
        login.login_into_app(Constants.USER_NAME, Constants.USER_PASSWORD)

        # Home
        home = Home(driver=driver, config=config)
        home.open_search_screen()

        # Search
        search = Search(driver=driver, config=config)

        yield search

    @allure.title("Verify that user is able to open search screen, TC_SEARCH_001")
    def test_open_search_view(self, search_view, config):
        assert search_view.fitness_image_visibility()
        assert search_view.online_image_visibility()
        search_view.scroll_to_bottom(config)
        assert search_view.wellness_image_visibility()
        assert search_view.beauty_image_visibility()

    @allure.title("Verify that user is able to open fitness category from search screen, TC_SEARCH_002")
    def test_open_fitness_view(self, search_view, driver, config):
        search_view.scroll_to_top()
        search_view.open_fitness()
        fitness = Fitness(driver=driver, config=config)
        assert search_view.fitness_image_invisibility()
        assert fitness.keyword_search_bar.text == Constants.FITNESS


class TestFitnessView:
    @pytest.fixture(scope="class")
    def fitness_view(self, driver, config):
        fitness = Fitness(driver=driver, config=config)
        if config.platform_name == "android":
            navigation = Navigation(driver=driver, config=config)
            navigation.swipe_left()
        yield fitness

    @allure.title("Filters bar: Verify that 'View by time', 'Time', 'Credits', 'Favorited', 'Amenities' pills are "
                  "available on filters bar, TC_SEARCH_003")
    def test_fitness_pills(self, fitness_view):
        assert fitness_view.view_by_the_time_button_visibility()
        assert fitness_view.time_button_visibility()
        fitness_view.swipe_left_from_time_button()
        assert fitness_view.credits_button_visibility()
        assert fitness_view.favorites_button_visibility()
        assert fitness_view.amenities_button_visibility()
