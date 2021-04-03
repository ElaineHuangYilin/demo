import os
from behave import fixture
from appium import webdriver

@fixture
def observatory_driver(context):
    try:
        platform = os.getenv('PLATFORM')
        desired_caps = create_desired_caps(platform)
        context.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        yield context
    finally:
        context.driver.close_app()

def create_ios_desired_caps():
    platform_version = os.getenv('IOS_DEVICE_PLATFORM_VERSION')
    device_name = os.getenv('IOS_DEVICE_NAME')
    xcode_orgid = os.getenv('IOS_XCODE_ORGID')

    desired_caps = {}
    desired_caps['platformName'] = 'iOS'
    desired_caps['platformVersion'] = platform_version
    desired_caps['automationName'] = 'XCUITest'
    desired_caps['deviceName'] = device_name
    desired_caps['bundleId'] = 'locspc'
    desired_caps["udid"] = "auto"
    desired_caps["xcodeOrgId"] = xcode_orgid
    desired_caps["xcodeSigningId"] = "iPhone Developer"
    desired_caps["updatedWDABundleId"] = 'io.appium.WebDriverAgentRunner'
    desired_caps['noReset'] = True

    return desired_caps

def create_android_desired_caps():
    platform_version = os.getenv('Android_DEVICE_PLATFORM_VERSION')
    device_name = os.getenv('Android_DEVICE_NAME')
    app = os.getenv('Android_DEVICE_APP')

    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = platform_version
    desired_caps['deviceName'] = device_name
    desired_caps['app'] = app
    desired_caps['appPackage'] = 'hko.MyObservatory_v1_0'
    desired_caps['noReset'] = True

    return desired_caps

def create_desired_caps(platform='iOS'):
    mapping = {
        'iOS': create_ios_desired_caps,
        'android': create_android_desired_caps
    }

    return mapping[platform]()
