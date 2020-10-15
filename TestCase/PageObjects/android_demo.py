# -*- encoding=utf8 -*-
__author__ = "BSTester"

from airobots.core.api import *
from unittest import TestCase
import os


class DemoOP(TestCase):
    def __init__(self, driver):
        super(DemoOP, self).__init__()
        self.poco = driver

    """Demo page objects."""
    def wake_up_and_open_calc(self):
        wake()
        keyevent("HOME")
        start_app('com.meizu.flyme.calculator')

    def calc_add(self):
        touch(Template(os.path.join(os.path.dirname(__file__), "tpl1602698317745.png"), record_pos=(-0.351, -0.026), resolution=(720, 1280)))
        self.poco(text="1").click()
        touch(Template(os.path.join(os.path.dirname(__file__), "tpl1602700388209.png"), record_pos=(0.331, 0.554), resolution=(720, 1280)))
        self.poco(text="1").click()
        touch(Template(os.path.join(os.path.dirname(__file__), "tpl1602700724083.png"), record_pos=(0.332, 0.76), resolution=(720, 1280)))
        sleep(2)

    def calc_c(self):
        touch(Template(os.path.join(os.path.dirname(__file__), "tpl1602698317745.png"), record_pos=(-0.351, -0.026), resolution=(720, 1280)))
        sleep(2)

    def close_calc(self):
        stop_app('com.meizu.flyme.calculator')
