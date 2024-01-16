#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time ： 2024/1/16 0016 14:24
@Auth ： Xq
@File ：other.py
@IDE ：PyCharm
"""
from sanic import Blueprint, text

other_api = Blueprint("other_api", url_prefix="/other")


@other_api.route('/')
async def other(request):
    """
    其他蓝图
    """
    return text("这是请求的其他")
