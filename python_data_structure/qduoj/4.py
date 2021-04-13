# -*- coding: utf-8 -*-


info = {
    1: 1,
    2: 1
}


def get_fob(n):
    if info.get(n):
        return info[n]
    else:
        info[n] = get_fob(n-1) + get_fob(n-2)
        return info[n]


while True:
    try:
        n = int(input().strip())
        print(get_fob(n))
    except:
        break
