# -*- coding: utf-8 -*-


def binary_search_left(times: list, pt):
    left = 0
    right = len(times) - 1
    while left <= right:
        mid = left + (right - left)//2
        if pt > times[mid]:
            left = mid + 1
        else:
            right = mid - 1
    if left == 0:
        return 0
    return left


def binary_search_right(times: list, pt):
    left = 0
    right = len(times) - 1
    while left <= right:
        mid = left + (right - left)//2
        if times[mid] <= pt:
            left = mid + 1
        else:
            right = mid - 1
    return right + 1


ll = [1, 1, 3, 3, 4, 6, 7, 8, 9, 10, 12]
lf = binary_search_left(ll, 3)
print(lf)
rh = binary_search_right(ll, 4)
print(rh)
print(ll[lf:rh])
