#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time ： 2024/1/16 0016 14:23
@Auth ： Xq
@File ：MysqlBlue.py
@IDE ：PyCharm
"""
from sanic import Blueprint, text, json
from UtilTools.DatabaseTools.MysqlTool import MySqlCurd

mysql_api = Blueprint("mysql_api", url_prefix="/mysql")


@mysql_api.get('/')
async def run(request):
    """
    mysql请求根目录
    """
    return text("这是请求的mysql的根目录")


@mysql_api.get('/select_now_database')
async def select_now_database(request):
    """
    查询数据库版本
    """
    MSC = MySqlCurd()
    try:
        data = MSC.select_version()
        result = {"code": 200, "data": data}
        return json(result)
    except Exception as e:
        result = {"code": 0, "data": e}
        return json(result)
