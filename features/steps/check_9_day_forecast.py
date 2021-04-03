# pylint: disable=undefined-variable, unused-argument

import json

from features.steps.check_weather_setup.check_9_day_forecast_setup_platform \
    import create_check_9_day_forecast_platform_helper

@given('在主页面点击左上角的菜单按钮')
def click_navigation_tab_in_home(context):
    helper = create_check_9_day_forecast_platform_helper(context.driver)
    menu_left_side_pannel_ele = helper.menu_left_side_pannel_ele()
    menu_left_side_pannel_ele.click()

@when('在导航栏点击九天天气预报')
def click_9_day_forecast_navigation_tab(context):
    helper = create_check_9_day_forecast_platform_helper(context.driver)
    forecast_ele = helper.forecast_ele()
    forecast_ele.click()

@then('明天的天气应该会显示')
def verify_tomorrow_weather(context):
    helper = create_check_9_day_forecast_platform_helper(context.driver)
    flag = False
    flag = helper.verify_tomorrow_weather()
    assert flag is True


@then('九天天气预报接口的respone status应该是200')
def verift_weather_api(context):
    helper = create_check_9_day_forecast_platform_helper(context.driver)
    helper.forecast_page_tab_ele()
    with open('api_status_data.json', 'r') as file:
        api_status_data = json.load(file)
    assert api_status_data == 200

@then('后天的relative humidity将会显示')
def verift_day_after_tomorrow_weather_info(context):
    with open('forecast_detail_data.json', 'r') as file:
        forecast_detail_data = json.load(file)
    assert forecast_detail_data[1]['max_rh'] is not None
    assert forecast_detail_data[1]['min_rh'] is not None
