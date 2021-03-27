# -*- encoding=utf8 -*-
__author__ = "BSTester"

from airobots.core.api import *
from unittest import TestCase
from TestCases.IOSCase import poco
import os


class DemoOP(TestCase):
    AC = Template(os.path.join(os.path.dirname(__file__), "tpl1616595316971.png"))
    C = '清除'
    ADD = Template(os.path.join(os.path.dirname(__file__), "tpl1616595335164.png"))
    EQ = Template(os.path.join(os.path.dirname(__file__), "tpl1616595352028.png"))

    """Demo page objects."""
    def wake_up_and_open_calc(self):
        home()
        start_app('com.apple.calculator')

    def calc_add(self):
        touch(self.AC)
        poco("1").click()
        touch(self.ADD)
        poco("1").click()
        touch(self.EQ)

    def calc_c(self):
        poco(self.C).click()

    def close_calc(self):
        stop_app('com.apple.calculator')



