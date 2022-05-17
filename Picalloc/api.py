# -*- coding:utf-8 -*-

import hmac
import time
import uuid
from hashlib import sha256

import requests

proxy = None
token = None


def get_headers(url, method):
    now = str(int(time.time()))
    nonce = str(uuid.uuid4()).replace('-', '')
    key = b'~d}$Q7$eIni=V)9\\RK/P.RM4;9[7|@/CA}b~OW!3?EV`:<>M7pddUBL5n|0/*Cn'
    msg = f'{url}{now}{nonce}{method}c69baf41da5abd1ffedc6d2fea56b'.encode()
    signature = hmac.new(key, msg, digestmod=sha256).hexdigest()
    headers = {
        "accept": 'application/vnd.picacomic.com.v1+json',
        "api-key": 'C69BAF41DA5ABD1FFEDC6D2FEA56B',
        "app-build-version": '45',
        "app-channel": '3',
        "app-platform": 'android',
        "app-uuid": 'defaultUuid',
        "app-version": '2.2.1.3.3.4',
        "image-quality": 'original',
        "nonce": nonce,
        "signature": signature,
        "time": now,
        "user-agent": 'okhttp/3.8.1',
    }

    if method == 'post':
        headers['content-type'] = 'application/json; charset=UTF-8'

    if token is not None:
        headers["authorization"] = token

    return headers


def request_get(url, **args):
    args['headers'] = get_headers(url, 'get')
    args['timeout'] = 60000

    if proxy is not None:
        args['proxies'] = {
            'http': proxy,
            'https': proxy,
        }

    try:
        response = requests.get(f'https://picaapi.picacomic.com/{url}', **args)

        if response.status_code == 200:
            return response.json()['data']
    except:
        pass

    return None


def request_post(url, **args):
    args['headers'] = get_headers(url, 'post')
    args['timeout'] = 60000

    if proxy is not None:
        args['proxies'] = {
            'http': proxy,
            'https': proxy,
        }

    try:
        response = requests.post(f'https://picaapi.picacomic.com/{url}', **args)

        if response.status_code == 200:
            return response.json()['data']
    except:
        pass

    return None


def login(username, password):
    return request_post('auth/sign-in', json={
        "email": username,
        "password": password,
    })


def search(keyword, page):
    return request_post(f'comics/advanced-search?page={page}', json={
        'keyword': keyword,
    })


def comic_info(comic):
    return request_get(f'comics/{comic}')


def comic_eps(comic, page):
    return request_get(f'comics/{comic}/eps?page={page}')


def comic_pic(comic, eps, page):
    return request_get(f'comics/{comic}/order/{eps}/pages?page={page}')


def comic_recom(comic):
    return request_get(f'comics/{comic}/recommendation')


def keywords():
    return request_get('keywords')


def random():
    return request_get('comics/random')
