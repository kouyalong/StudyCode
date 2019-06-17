#!/usr/bin/python
# coding: utf-8

import timeit
import math


print(math.sqrt(2))
print(math.pow(10, 3))


def my_pow(x, y):
    number = 1
    while y:
        if y & 1:
            number *= x
        y >>= 1
        x *= x
    return number


def func(a, b):
    r = 1
    while b > 1:
        if b & 1 == 1:  #与运算一般可以用于取某位数，这里就是取最后一位。
            r *= a
        a *= a
        b = b >> 1 #这里等价于b//=2
    ret = r * a
    return ret


def math_pow(x, y):
    ret = math.pow(x, y)
    return ret


print(timeit.timeit("func(33, 33)", setup="from __main__ import func"))
print(timeit.timeit("my_pow(33, 33)", setup="from __main__ import my_pow"))
print(timeit.timeit("math_pow(33, 33)", setup="from __main__ import math_pow"))
