#!/usr/bin/python
# coding: utf-8


def binary_search(arr, l, r, x):
    # 基本判断
    if r >= l:

        mid = int(l + (r - l) / 2)

        # 元素整好的中间位置
        if arr[mid] == x:
            return mid

            # 元素小于中间位置的元素，只需要再比较左边的元素
        elif arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)

            # 元素大于中间位置的元素，只需要再比较右边的元素
        else:
            return binary_search(arr, mid + 1, r, x)

    else:
        # 不存在
        print(l, r)
        return -1-l


ll = [1, 4, 5, 6, 12]
print(binary_search(ll, 0, len(ll), 9))
