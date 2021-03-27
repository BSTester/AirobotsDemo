# -*- encoding=utf8 -*-
__author__ = "BSTester"

from airobots.core.api import *
from unittest import TestCase
from TestCases.IOSCase import driver
import os


class DemoOP(TestCase):
    AC = '全部清除'
    C = '清除'
    ADD = '//XCUIElementTypeButton[@name="加"]'
    EQ = '等于'

    """Demo page objects."""

    def calc_add(self):
        driver.click_button(self.AC)
        driver.click_text(1)
        driver.click_element(self.ADD)
        driver.click_text(1)
        driver.click_button(self.EQ)

    def calc_c(self):
        driver.click_button(self.C)

    def close_calc(self):
        driver.quit_application()



