#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time ： 2024/1/16 0016 14:29
@Auth ： Xq
@File ：runsreve.py
@IDE ：PyCharm
"""
from sanic import Sanic
from sanic.response import json
from Blues import blues

app = Sanic("henan_oms_sanic_config")
app.blueprint(blues)


@app.get('/')
async def run(request):
    """
    主页
    """
    res = {"data": {"id": 1, "msg": {"hello": "sanic"}, "code": 200}}

    return json(res)


@app.get('/get')
async def get(request):
    """
    主函数get请求
    """
    print(request.query_args)
    res = {"data": {"id": 1, "msg": {"hello": "sanic"}, "code": 200}}

    return json(res)


@app.post('/post')
async def post(request):
    """
    主函数post请求
    """
    response = eval(request.body.decode("utf-8"))
    if response.get('user') == "admin" and response.get("password") == "admin":
        res = {"data": {"code": 200, "hello": "post"}}
        return json(res)
    else:
        res = {"data": {"code": 400, "hello": "post"}}
        return json(res)


if __name__ == '__main__':
    # app.run(host="127.0.0.1", port=8000)
    app.run(host="localhost", port=8000)
