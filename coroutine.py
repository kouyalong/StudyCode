#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time


def task1():
    while True:
        yield "<甲>也累了，让<乙>工作一会儿"
        time.sleep(4)
        print("<甲>工作了一段时间.....")


def task2(t):
    next(t)
    while True:
        print("-----------------------------------")
        print("<乙>工作了一段时间.....")
        time.sleep(2)
        print("<乙>累了，让<甲>工作一会儿....")
        ret = t.send(None)
        print(ret)
    t.close()



def fib(n):
    a, b = 0, 1
    i = 0
    while i < n:
        yield b
        a, b = b, a+b
        i += 1

if __name__ == '__main__':
    # t = task1()
    # task2(t)

    for number in fib(5):
        print(number)

