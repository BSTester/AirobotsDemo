# -*- encoding=utf8 -*-

from airtest.core.api import *
from unittest import TestCase
from airtest.core.settings import Settings as ST
from airobotLibrary import AirSelenium
from pathlib import Path

TPL_PATH = Path(__file__).parent

class DemoOP(TestCase):
    """Demo page objects."""

    SEARCH_BOX = '//*[@id="kw"]'
    SEARCH_BUTTON = '//*[@id="su"]'
    # SEARCH_BUTTON = Template(Path.joinpath(TPL_PATH, 'baidu.png'))
    # HOME_LOGO = Template(Path.joinpath(TPL_PATH, 'baidu_logo.png'))
    LINK = '//div/h3/a[contains(string(), "{}")]'
    
    def __init__(self, driver):
        super(DemoOP, self).__init__()
        self.wd = driver or AirSelenium()

    def input_keywords(self, text):
        self.wd.input_text(self.SEARCH_BOX, text=text)

    def click_search_button(self):
        # self.wd.driver.airtest_touch(self.SEARCH_BUTTON)
        self.wd.click_button(self.SEARCH_BUTTON)

    def search(self, text):
        self.input_keywords(text=text)
        self.click_search_button()
        sleep(1)

    def search_and_click(self, text, click_text):
        self.search(text)
        # self.wd.driver.airtest_touch(self.HOME_LOGO)
        # sleep(1)
        # self.search(text)
        self.wd.set_focus_to_element(self.LINK.format(click_text))
        self.wd.click_link(self.LINK.format(click_text))