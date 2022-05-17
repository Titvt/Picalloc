# -*- coding:utf-8 -*-

import json

from flask import Flask, request, render_template

import api

try:
    with open('config.json', 'rb') as f:
        config = json.load(f)

    api.proxy = config['proxy'] if 'proxy' in config else None
    api.token = api.login(config['username'], config['password'])['token']
except:
    exit(0)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/auth', methods=['POST'])
def auth():
    while True:
        key = request.form.get('key')

        if key is None:
            break

        if key != (config['key'] if 'key' in config else ''):
            break

        return {
            'status': 'ok',
        }

    return {
        'status': 'error',
    }


@app.route('/search', methods=['POST'])
def search():
    while True:
        keyword = request.form.get('keyword')
        page = request.form.get('page')

        if keyword is None or page is None:
            break

        data = api.search(keyword, page)

        if data is None:
            break

        return {
            'data': {
                'comicList': [
                    {
                        'name': i['title'],
                        'comic': i['_id'],
                        'cover': f"{i['thumb']['fileServer']}/static/{i['thumb']['path']}",
                        'author': i['author'] if 'author' in i else '',
                        'likeCount': i['likesCount'],
                    }
                    for i in data['comics']['docs']
                ],
                'pageCount': data['comics']['pages'],
                'comicCount': data['comics']['total'],
            },
            'status': 'ok',
        }

    return {
        'status': 'error',
    }


@app.route('/comic_info', methods=['POST'])
def comic_info():
    while True:
        comic = request.form.get('comic')

        if comic is None:
            break

        data = api.comic_info(comic)

        if data is None:
            break

        return {
            'data': {
                'name': data['comic']['title'],
                'tags': data['comic']['tags'],
                'comic': data['comic']['_id'],
                'cover': f"{data['comic']['thumb']['fileServer']}/static/{data['comic']['thumb']['path']}",
                'author': data['comic']['author'] if 'author' in data['comic'] else '',
                'likeCount': data['comic']['likesCount'],
                'description': data['comic']['description'] if 'description' in data['comic'] else '',
                'pictureCount': data['comic']['pagesCount'],
            },
            'status': 'ok',
        }

    return {
        'status': 'error',
    }


@app.route('/comic_eps', methods=['POST'])
def comic_eps():
    while True:
        comic = request.form.get('comic')
        page = request.form.get('page')

        if comic is None or page is None:
            break

        data = api.comic_eps(comic, page)

        if data is None:
            break

        return {
            'data': {
                'epsList': [
                    {
                        'eps': i['order'],
                        'name': i['title'],
                    }
                    for i in data['eps']['docs']
                ],
                'epsCount': data['eps']['total'],
                'pageCount': data['eps']['pages'],
            },
            'status': 'ok',
        }

    return {
        'status': 'error',
    }


@app.route('/comic_pic', methods=['POST'])
def comic_pic():
    while True:
        comic = request.form.get('comic')
        eps = request.form.get('eps')
        page = request.form.get('page')

        if comic is None or eps is None or page is None:
            break

        data = api.comic_pic(comic, eps, page)

        if data is None:
            break

        return {
            'data': {
                'pageCount': data['pages']['pages'],
                'pictureList': [
                    f"{i['media']['fileServer']}/static/{i['media']['path']}"
                    for i in data['pages']['docs']
                ],
                'pictureCount': data['pages']['total'],
            },
            'status': 'ok',
        }

    return {
        'status': 'error',
    }


@app.route('/comic_recom', methods=['POST'])
def comic_recom():
    while True:
        comic = request.form.get('comic')

        if comic is None:
            break

        data = api.comic_recom(comic)

        if data is None:
            break

        return {
            'data': [
                {
                    'name': i['title'],
                    'comic': i['_id'],
                    'cover': f"{i['thumb']['fileServer']}/static/{i['thumb']['path']}",
                    'author': i['author'] if 'author' in i else '',
                    'likeCount': i['likesCount'],
                }
                for i in data['comics']
            ],
            'status': 'ok',
        }

    return {
        'status': 'error',
    }


@app.route('/keywords', methods=['POST'])
def keywords():
    while True:
        data = api.keywords()

        if data is None:
            break

        return {
            'data': [
                i
                for i in data['keywords']
            ],
            'status': 'ok',
        }

    return {
        'status': 'error',
    }


@app.route('/random', methods=['POST'])
def random():
    while True:
        data = api.random()

        if data is None:
            break

        return {
            'data': [
                {
                    'name': i['title'],
                    'comic': i['_id'],
                    'cover': f"{i['thumb']['fileServer']}/static/{i['thumb']['path']}",
                    'author': i['author'] if 'author' in i else '',
                    'likeCount': i['likesCount'],
                }
                for i in data['comics']
            ],
            'status': 'ok',
        }

    return {
        'status': 'error',
    }
