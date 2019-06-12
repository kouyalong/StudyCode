#!/usr/bin/python
# coding: utf-8


def binary_search(l, start, end, item):
    # 从小到大的顺序 二分查找 首次出现的位置
    if l:
        mid = (start + end) // 2

        if l[mid] < item:
            end = mid - 1
            return binary_search(l, start, end, item)
        elif l[mid] > item:
            start = mid + 1
            return binary_search(l, start, end, item)
        else:
            # return mid
            for i in range(mid, -1, -1):
                if l[i] < item:
                    return i + 1
                else:
                    continue


ll = [1, 2, 3, 3, 3, 3, 4, 5, 6]
print(binary_search(ll, 0, len(ll), 3))
