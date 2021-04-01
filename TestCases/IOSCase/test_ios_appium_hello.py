# -*- encoding=utf8 -*-

from airobots.core.api import *
from unittest import TestCase
from airobots.core.settings import ST
from TestCases.PageObjects.IOS.ios_appium_demo import DemoOP
from TestCases.IOSCase import driver
import os


class IOSCase(TestCase):
    """Custom launcher."""

    @classmethod
    def setUpClass(cls):
        super(IOSCase, cls).setUpClass()
        cls.ios = DemoOP()

    def setUp(self):
        """Custom setup logic here."""
        # add var/function/class/.. to globals:
        # self.scope["add"] = lambda x: x+1
        # exec setup test script:
        # self.exec_other_script("setup.air")
        # set custom parameter in Settings:
        # ST.THRESHOLD = 0.75
        super(IOSCase, self).setUp()

    def tearDown(self):
        """Custom tear down logic here."""
        # exec teardown script:
        # self.exec_other_script("teardown.air")
        super(IOSCase, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        super(IOSCase, cls).tearDownClass()

    def test_calc(self):
        self.ios.calc_add()
        driver.element_value_should_be('结果', 2)
        self.ios.calc_c()
        self.ios.close_calc()
