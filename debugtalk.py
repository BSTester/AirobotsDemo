import time
import os
import json
import requests
from urllib.parse import urlencode
from httprunner import __version__


def now_time():
    return time.strftime('%Y%m%dT%H%M%S')


def get_httprunner_version():
    return __version__


def get_ticket(url):
    try:
        return url.split('?')[1].split('=')[1]
    except Exception as e:
        return ''
