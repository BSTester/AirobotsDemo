# NOTICE: Generated By HttpRunner. DO NOT EDIT!
from airobots.poco.ios import IOSUiautomation
from airobots.robot import AirAppium
from airobots.core.api import connect_device


# 基于poco
poco = IOSUiautomation(device=connect_device('iOS:///127.0.0.1:8100'), use_airtest_input=True, screenshot_each_action=False)

# 基于appium
# driver = AirAppium()
# driver.open_application(remote_url='http://localhost:4723/wd/hub', bundleId='com.apple.calculator', platformName='iOS', platformVersion='14.4.1', deviceName="Penn's iPhone", udid='6f004f4eb3528659c9c617836e698cb7e5a21605')
