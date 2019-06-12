#!/usr/bin/python
# coding: utf-8

import requests
import json


def tt_ll():
    url = "http://0.0.0.0:9985/v1/assign"
    data = {"job_id": 1, "task_pool_id": 1, "now": 1}
    ret = requests.post(url, data=json.dumps(data))
    print(ret.content)


a = 3


def f():
    a = 4
    print(a)

    def v():
        print a
    return v


t = f()
print("ttt")
t()
print(a)


def change(x, l=[]):
    print("before", l, id(l))
    for i in range(x):
        l.append(i*i)
    print("after", l, id(l))
    return l


change(2)
change(1, [2])
change(3)

