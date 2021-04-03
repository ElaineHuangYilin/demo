功能: 测试九天预报明天和后天的天气

    #执行测试前，需执行mitmdump -s mitmproxy.py启动数据浏览监听
    @fixture.observatory_driver
    场景: 九天天气预报，明后天的天气应该正常显示
        假如 在主页面点击左上角的菜单按钮
        当 在导航栏点击九天天气预报
        那么 明天的天气应该会显示
        那么 九天天气预报接口的respone status应该是200
        那么 后天的relative humidity将会显示