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

def get_token(base_url):
    system_name = system_uri = 'ehr-admin'
    resp = requests.post('{}/teacore/teaCoreSso/ssoLogin'.format(base_url), json=dict(
        params=dict(username=os.environ.get('USERNAME', '') if base_url.find('pre-api') == -1 else os.environ.get('USERNAME_PRE', ''), 
        password=os.environ.get('PASSWORD', '') if base_url.find('pre-api') == -1 else os.environ.get('PASSWORD_PRE', '')), type=0, redirectUrl=base_url, sysName=system_name))
    token = ''
    if resp.status_code != 200: return token
    body = json.loads(resp.content)
    if body.get('code') != 303: return token
    # redirect_url = body.get('data').get('redirectUrl')
    # resp = requests.get('{}/{}/teaCoreSsoClient/getInfo?ticket={}'.format(base_url, system_uri, get_ticket(redirect_url)))
    # if resp.status_code != 200: return token
    # body = json.loads(resp.content)
    # if body.get('code') != 200: return token
    token = body.get('data').get('token')
    return token

def get_h5_token(base_url):
    system_name = system_uri = 'ehr-entrant'
    token = ''
    offer_system_name = offer_system_uri = 'ehr-admin'
    # resp = requests.post('{}/{}/ivva/callbackCancelEntry'.format(base_url, offer_system_uri), headers={"Content-Type": "application/x-www-form-urlencoded"}, data=urlencode(dict(positionId=10475, recruitId=719452, resumeId=1812021, isSchoolRecruit=0, status=2)))
    # if resp.status_code != 200: return token
    # body = json.loads(resp.content)
    # if body.get('success') != True: return token
    resp = requests.post('{}/{}/ivva/callbackAcceptOffer'.format(base_url, offer_system_uri), headers={"Content-Type": "application/x-www-form-urlencoded"}, data=urlencode(dict(positionId=10475, recruitId=719452, resumeId=1812021, offerSendLogsId=3244, replyStatus=1)))
    if resp.status_code != 200: return token
    # body = json.loads(resp.content)
    # if body.get('success') != True: return token
    # resp = requests.post('{}/{}/getVerificationCode'.format(base_url, system_uri), json=dict(mobile=os.environ.get('MOBILE', '')))
    # if resp.status_code != 200: return token
    # body = json.loads(resp.content)
    # if body.get('code') != 0: return token
    resp = requests.post('{}/{}/login'.format(base_url, system_uri), json=dict(mobile=os.environ.get('MOBILE', ''), verificationCode=os.environ.get('CODE', '')))
    if resp.status_code != 200: return token
    body = json.loads(resp.content)
    if body.get('code') != 0: return token
    token = body.get('data')
    return token

