# -*- coding: utf-8 -*-

import base64

str_36 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def baseN(num, b):
    return ((num == 0) and "0") or \
           (baseN(num // b, b).lstrip("0") + str_36[num % b])


def to_256(nums):
    res = 0
    x = (1 << 0)
    for n in nums[::-1]:
        res += n * x
        x = x << 8
    return res


b64 = base64.b64decode(input())

byte_array = [x for x in bytearray(b64)]
sn = to_256(byte_array)
print(baseN(sn, 36))
