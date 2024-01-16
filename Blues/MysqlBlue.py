#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time ： 2024/1/16 0016 14:23
@Auth ： Xq
@File ：MysqlBlue.py
@IDE ：PyCharm
"""
from sanic import Blueprint, text, json

mysql_api = Blueprint("mysql_api", url_prefix="/mysql")


@mysql_api.get('/')
async def run(request):
    """
    mysql请求根目录
    """
    return text("这是请求的mysql")


@mysql_api.get('/get1')
async def get(request):
    """
    mysql 请求
    """
    return text("这是请求的mysql查询")
