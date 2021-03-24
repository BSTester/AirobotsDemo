# -*- encoding=utf8 -*-
__author__ = "BSTester"

from airobots.core.api import *
from unittest import TestCase
from TestCases.IOSCase import driver
import os


class DemoOP(TestCase):
    def __init__(self, driver=driver):
        super(DemoOP, self).__init__()
        self.poco = driver

    """Demo page objects."""
    def wake_up_and_open_calc(self):
        home()
        start_app('com.apple.calculator')

    def calc_add(self):
        touch(Template(os.path.join(os.path.dirname(__file__), "tpl1616595316971.png")))
        self.poco("1").click()
        touch(Template(os.path.join(os.path.dirname(__file__), "tpl1616595335164.png")))
        self.poco("1").click()
        touch(Template(os.path.join(os.path.dirname(__file__), "tpl1616595352028.png")))

    def calc_c(self):
        touch(Template(os.path.join(os.path.dirname(__file__), "tpl1616595316971.png")))

    def close_calc(self):
        stop_app('com.apple.calculator')



