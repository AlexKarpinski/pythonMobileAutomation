# Python Mobile Automation Framework

A Python-based mobile automation testing framework using Appium and Pytest for testing mobile applications on both Android and iOS platforms.

## Overview

This framework implements the Page Object Model (POM) design pattern to create maintainable and reusable automated tests for mobile applications. It supports both Android and iOS platforms and provides a structured approach to mobile test automation.

## Features

- **Cross-platform support**: Test on both Android and iOS devices
- **Page Object Model**: Clean separation of test logic and page elements
- **Pytest integration**: Powerful test execution and reporting
- **Appium WebDriver**: Industry-standard mobile automation
- **Allure reporting**: Generate detailed test reports
- **Configurable environments**: Support for multiple test environments (QA, STG)
- **Device configuration**: Flexible device and capability management

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.9 or higher
- Appium Server (for mobile automation)
- Android SDK and Android Emulator (for Android testing)
- Xcode and iOS Simulator (for iOS testing on macOS)
- pipenv (for dependency management)

### Setting up Appium

1. Install Node.js and npm
2. Install Appium globally:
   ```bash
   npm install -g appium
   ```
3. Start Appium server:
   ```bash
   appium
   ```
   The server will run on `http://0.0.0.0:4723` by default.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AlexKarpinski/pythonMobileAutomation.git
   cd pythonMobileAutomation
   ```

2. Install dependencies using pipenv:
   ```bash
   pipenv install
   ```

3. Activate the virtual environment:
   ```bash
   pipenv shell
   ```

## Configuration

### Device Configuration

The framework supports multiple device configurations defined in `page_object/desired_capabilities.py`. Currently configured devices:

- **EMULATOR_ANDROID**: Android emulator (Pixel 3A, Android 10)
- **MAC_MINI_LOCAL_IPHONE_XR**: iOS device (iPhone XR, iOS 14.4+)

To add a new device, add a new configuration in the `DesiredCapabilities` class with the appropriate capabilities for your device.

### Environment Configuration

The framework supports different environments (QA, STG) which can be specified when running tests. Configuration is managed through:

- `page_object/config.py`: Main configuration classes
- `page_object/data/constants.py`: Test data and constants

## Project Structure

```
pythonMobileAutomation/
├── page_object/              # Page Object Model implementation
│   ├── data/                 # Test data and constants
│   ├── locators/             # Element locators for different pages
│   │   ├── fitness/          # Fitness-related locators
│   │   ├── home_locators.py
│   │   ├── login_locators.py
│   │   ├── profile_locators.py
│   │   └── search_locators.py
│   ├── views/                # Page object classes
│   │   ├── fitness/          # Fitness-related views
│   │   ├── base_view.py      # Base view with common methods
│   │   ├── home_view.py
│   │   ├── login_view.py
│   │   ├── profile_view.py
│   │   └── search_view.py
│   ├── base_element.py       # Base element wrapper
│   ├── config.py             # Configuration management
│   ├── desired_capabilities.py  # Device capabilities
│   └── locator.py            # Locator utilities
├── tests/                    # Test files
│   ├── conftest.py           # Pytest fixtures and configuration
│   ├── login_test.py         # Login functionality tests
│   └── search_test.py        # Search functionality tests
├── webdriver/                # WebDriver utilities
│   └── webdriver.py          # WebDriver initialization
├── Pipfile                   # Project dependencies
└── main.py                   # Sample entry point
```

## Running Tests

### Basic Test Execution

Run tests with required device specification:

```bash
pytest --device-name=EMULATOR_ANDROID
```

### Specify Environment

Run tests against a specific environment (default is QA):

```bash
pytest --device-name=EMULATOR_ANDROID --env=qa
```

### Run Specific Test File

```bash
pytest tests/login_test.py --device-name=EMULATOR_ANDROID
```

### Run Specific Test

```bash
pytest tests/login_test.py::TestLoginView::test_login_positive --device-name=EMULATOR_ANDROID
```

### Run with Build Number (for Kobiton)

```bash
pytest --device-name=EMULATOR_ANDROID --build=123
```

## Writing Tests

### Test Structure Example

```python
import pytest
from page_object.views.login_view import Login
from page_object.data.constants import Constants

class TestLogin:
    @pytest.fixture(scope="class")
    def login_view(self, driver, config):
        login = Login(driver=driver, config=config)
        yield login

    def test_login_positive(self, login_view):
        login_view.login_into_app(Constants.USER_NAME, Constants.USER_PASSWORD)
        assert login_view.login_button_invisibility()
```

### Page Object Example

```python
from page_object.views.base_view import BaseView
from page_object.locators.login_locators import LoginLocators

class Login(BaseView):
    def __init__(self, driver, config):
        super().__init__(driver, config)
        self.locator = LoginLocators

    def login_into_app(self, username, password):
        # Implementation
        pass
```

## Test Fixtures

The framework provides several pytest fixtures defined in `tests/conftest.py`:

- `driver`: WebDriver session (session scope)
- `config`: Test configuration object
- `env_config`: Environment configuration
- `device_config`: Device configuration
- `test_config`: Test-specific configuration

## Command Line Options

- `--env`: Environment to run tests against (default: qa)
- `--device-name`: Device name from desired capabilities (required)
- `--build`: Build number for Kobiton (default: 0)

## Available Test Markers

- `skip_platform`: Skip tests on specific platforms
  ```python
  @pytest.mark.skip_platform('ios', 'iOS specific issue')
  def test_example(self):
      pass
  ```

## Dependencies

Main dependencies (defined in Pipfile):

- `pytest`: Testing framework
- `appium-python-client`: Appium Python client
- `selenium`: WebDriver library
- `allure-pytest`: Test reporting (if configured)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Ensure tests pass
5. Submit a pull request

## Troubleshooting

### Appium Server Connection Issues

- Ensure Appium server is running on `http://0.0.0.0:4723`
- Check that the device is properly configured and accessible
- Verify desired capabilities match your device configuration

### Device Not Found

- For Android: Verify emulator is running (`adb devices`)
- For iOS: Verify device UDID matches the configuration
- Check that the device name in the command matches a configuration in `desired_capabilities.py`

### Test Timeouts

- The framework waits up to 120 seconds for device connection (configured in `tests/conftest.py`, line 87)
- Individual element waits default to 5 seconds (can be adjusted per wait call or in `base_view.py`)
- Adjust the `wait_time` parameter in the driver fixture if you need longer device initialization times

## License

This project is available for educational and testing purposes.
