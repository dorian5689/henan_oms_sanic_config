#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time ： 2024/1/16 0016 14:05
@Auth ： Xq
@File ：DataBaseConfig.py
@IDE ：PyCharm
"""


def mysql__localhost_config():
    config_ = {
        'host': 'localhost',
        'port': '3306',
        'username': 'root',
        'password': '123456',
        'database': 'school'
    }
    return config_
