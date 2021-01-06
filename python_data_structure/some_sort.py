#!/usr/bin/python
# coding: utf-8


def bubble_sort(l):
    length = len(l)
    for i in range(length):
        for j in range(length):
            if l[i] < l[j]:
                l[i], l[j] = l[j], l[i]
    return l


def select_sort(l, end):
    max_j = 0
    for i in range(end):
        if l[max_j] < l[i]:
            max_j = i
        l[max_j], l[end-1] = l[end-1], l[max_j]
    if end > 0:
        return select_sort(l, end-1)
    return l


def insert_sort(l):
    for i in range(1, len(l)):
        if l[i-1] > l[i]:
            current = l[i]
            pos = i
            while pos > 0 and l[pos-1] > current:
                l[pos] = l[pos-1]
                pos -= 1
            l[pos] = current
    return l


def gap_insert_sort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        if alist[i-gap] > alist[i]:
            current = alist[i]
            pos = i
            while pos >= gap and alist[pos-gap]>current:
                alist[pos] = alist[pos-gap]
                pos -= gap
            alist[pos] = current


def shell_sort(l):
    sub_l = len(l) // 2

    while sub_l > 0:
        for sub in range(sub_l):
            gap_insert_sort(l, sub, sub_l)
        sub_l //= 2
    return l


def merge_sort(al):
    mid = len(al) // 2
    left, right = al[:mid], al[mid:]
    if len(left) > 1: left = merge_sort(left)
    if len(right) > 1: right = merge_sort(right)
    res = []
    while left and right:
        if left[-1] <= right[-1]:
            res.append(left.pop())
        else:
            res.append(right.pop())
    res.reverse()
    return (right or left) + res


def new_merge_sort(al):
    # 从小到大的归并排序
    if len(al) > 1:
        mid = len(al) // 2
        left, right = al[:mid], al[mid:]
        left = merge_sort(left)
        right = merge_sort(right)
        res = []
        while left and right:
            if left[-1] > right[-1]:
                res.append(right.pop())
            else:
                res.append(left.pop())
        while right:
            res.append(right.pop())
        while left:
            res.append(left.pop())
        return res
    return al


def new_merge_sort_reserve(al):
    # 从大到小的归并排序
    if len(al) > 1:
        mid = len(al) // 2
        left, right = al[:mid], al[mid:]
        left = merge_sort(left)
        right = merge_sort(right)
        res = []
        while left and right:
            if left[0] < right[0]:
                res.append(right.pop(0))
            else:
                res.append(left.pop(0))
        if right:
            res += right
        if left:
            res += left
        return res
    return al


def quick_sort(al):
    return quick_sort_de(al, 0, len(al)-1)


def quick_sort_de(al, first, last):
    if first < last:
        pos = partition(al, first, last)
        quick_sort_de(al, first, pos-1)
        quick_sort_de(al, pos+1, last)
    return al


def partition(al, first, last):
    value = al[first]

    left = first + 1
    right = last

    done = False
    while not done:
        while left <= right and al[left] >= value:
            left += 1
        while right >= left and al[right] <= value:
            right -= 1

        if right < left:
            done = True
        else:
            al[left], al[right] = al[right], al[left]
    al[first], al[right] = al[right], al[first]
    return right



ll = [7, 3, 1, 4, 6, 2, 5, 8, 9, 3]
# print(bubble_sort(ll))
# print(select_sort(ll, len(ll)))
# print(insert_sort(ll))
# print(shell_sort(ll))
# print(merge_sort(ll))
# print(new_merge_sort(ll))
# print(new_merge_sort_reserve(ll))
print(quick_sort(ll))