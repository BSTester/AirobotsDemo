# -*- encoding=utf8 -*-

from airobots.core.api import *
from unittest import TestCase
from airtest.core.settings import Settings as ST
from TestCase.PageObjects.android_demo import DemoOP
from airobots.poco.android import AndroidUiautomation
import os


class AndroidCase(TestCase):
    """Custom launcher."""

    @classmethod
    def setUpClass(cls):
        super(AndroidCase, cls).setUpClass()
        cls.poco = AndroidUiautomation(use_airtest_input=True, screenshot_each_action=False)
        cls.android = DemoOP(driver=cls.poco)

    def setUp(self):
        """Custom setup logic here."""
        # add var/function/class/.. to globals:
        # self.scope["add"] = lambda x: x+1
        # exec setup test script:
        # self.exec_other_script("setup.air")
        # set custom parameter in Settings:
        # ST.THRESHOLD = 0.75
        super(AndroidCase, self).setUp()

    def tearDown(self):
        """Custom tear down logic here."""
        # exec teardown script:
        # self.exec_other_script("teardown.air")
        super(AndroidCase, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        super(AndroidCase, cls).tearDownClass()

    def test_calc(self):
        self.android.wake_up_and_open_calc()
        self.android.calc_add()
        assert_exists(Template(os.path.join(os.path.dirname(__file__), "tpl1602777528520.png"), record_pos=(0.379, -0.267), resolution=(720, 1280)), "计算结果是否等于2")
        self.android.calc_c()
        self.android.close_calc()
