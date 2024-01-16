#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time ： 2024/1/16 0016 14:22
@Auth ： Xq
@File ：__init__.py.py
@IDE ：PyCharm
"""
from sanic import Blueprint
from Configs.BlueConfig import blues

api = Blueprint.group(blues, url_prefix="/api")