import os

import datetime

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from dotenv import load_dotenv



def create_check_9_day_forecast_platform_helper(driver):
    load_dotenv()
    mapping = {
        'iOS': Check9DayforecastSetupIOS,
        'android': Check9DayforecastSetupAndroid
    }

    return mapping[os.getenv('PLATFORM')](driver)

class Check9DayforecastSetupBase:
    def __init__(self, driver):
        self.driver = driver

    def menu_left_side_pannel_ele(self):
        raise 'should implement {}'.format(__name__)

    def forecast_ele(self):
        raise 'should implement {}'.format(__name__)

    def verify_tomorrow_weather(self):
        raise 'should implement {}'.format(__name__)


class Check9DayforecastSetupIOS(Check9DayforecastSetupBase):
    def menu_left_side_pannel_ele(self):
        wait = WebDriverWait(self.driver, 30)
        return wait.until(EC.element_to_be_clickable(
            (MobileBy.ACCESSIBILITY_ID, 'Menu, left side panel')))

    def forecast_ele(self):
        wait = WebDriverWait(self.driver, 30)
        return wait.until(EC.presence_of_element_located(
            (MobileBy.ACCESSIBILITY_ID, '9-Day Forecast')))

    def verify_tomorrow_weather(self):
        wait = WebDriverWait(self.driver, 30)
        today = datetime.date.today()
        tomorrow = (today + datetime.timedelta(days=1))
        correct_style_tomorrow = tomorrow.strftime("%Y/%m/%d", tomorrow)

        try:
            tomorrow_weather = wait.until(EC.presence_of_element_located(
                (By.XPATH,
                 '//XCUIElementTypeStaticText[starts-with(@name, '+correct_style_tomorrow+')]"]\
                     /following-sibling::XCUIElementTypeStaticText[1]')))

            assert tomorrow_weather.get_attribute('name') is not None
        except Exception:
            flag = False
        else:
            flag = True
        return flag

class Check9DayforecastSetupAndroid(Check9DayforecastSetupBase):
    def menu_left_side_pannel_ele(self):
        wait = WebDriverWait(self.driver, 30)
        return wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, '转到上一层级')))

    def forecast_ele(self):
        TouchAction(self.driver).press(x=699, y=1767).move_to(x=699, y=950).release().perform()
        wait = WebDriverWait(self.driver, 30)
        return wait.until(EC.presence_of_element_located((By.XPATH, '//*[@text="九天預報"]')))

    def verify_tomorrow_weather(self):
        wait = WebDriverWait(self.driver, 30)
        try:
            wait.until(EC.presence_of_element_located(
                (By.ID, 'hko.MyObservatory_v1_0:id/sevenDayLinearLayout')))
            tomorrow_weather_ele = self.driver.find_elements_by_id(
                "hko.MyObservatory_v1_0:id/sevenDayLinearLayout")[0]

            assert tomorrow_weather_ele.get_attribute('content-desc') is not None
        except Exception:
            flag = False
        else:
            flag = True
        return flag
