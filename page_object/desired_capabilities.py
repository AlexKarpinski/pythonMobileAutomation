class DesiredCapabilities(object):
    EMULATOR_ANDROID = {
        "platformName": "Android",
        "automationName": "UIAutomator2",
        "platformVersion": "10",
        "udid": "emulator-5554",
        "deviceName": "Pixel 3A",
        "appPackage": "com.classpass.classpass.dev",
        "appActivity": "com.classpass.classpass.appstart.viewcontrollers.activities.SplashScreenActivity",
        "autoGrantPermissions": True,
        "newCommandTimeout": 60,
        "systemPort": 8201
    }

    MAC_MINI_LOCAL_IPHONE_XR = {
        "platformName": "iOS",
        "xcodeSigningId": "Classpass Inc.",
        "udid": "00008020-001D15DC2691002E",
        "automationName": "XCUITest",
        "deviceName": "iPhone",
        "bundleId": "com.classpass.enterprise.development",
        "platformVersion": "14.4",
        "agentPath": "/usr/local/lib/node_modules/appium/node_modules/appium-webdriveragent/WebDriverAgent.xcodeproj",
        "newCommandTimeout": 360,
    }
