import allure
import pytest

from page_object.views.login_view import Login
from page_object.views.profile_view import Profile
from page_object.data.constants import Constants


class TestLoginView:

    @pytest.fixture(scope="class")
    def login_view(self, driver, config, env_config):
        # Log out
        if config.platform_name == "ios":
            profile = Profile(driver=driver, config=config)
            profile.log_out()

        # Log in
        login = Login(driver=driver, config=config)

        yield login

        # Log out
        profile = Profile(driver=driver, config=config)
        profile.log_out()

    @allure.title("Verify that user can't login to the app with non-existing email, TC_LOGIN_002")
    def test_login_negative(self, login_view):
        login_view.login_into_app(Constants.USER_NAME, Constants.INVALID_PASSWORD)
        message = login_view.unsuccessful_login_message.text
        assert message == Constants.UNSUCCESSFUL_LOGIN_MESSAGE_TEXT
        login_view.open_previous_screen()

    @allure.title("Verify that user can log in to the app with valid email and password, TC_LOGIN_001")
    def test_login_positive(self, login_view):
        login_view.login_into_app(Constants.USER_NAME, Constants.USER_PASSWORD)
        assert login_view.login_button_invisibility()
