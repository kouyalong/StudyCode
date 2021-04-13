# -*- coding: utf-8 -*-


def to_int(line: str):
    return [int(_n) for _n in line.split(" ")]


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


group_num = int(input())

for _ in range(group_num):
    log_count = int(input())
    log_times = []
    for _ in range(log_count):
        _log_time = int(input())
        log_times.append(_log_time)
    log_times.sort()
    section_num = int(input())
    for _ in range(section_num):
        section_time = to_int(input())
        start, end = section_time[0], section_time[1]
        start_index = binary_search_left(log_times, start-1)
        end_index = binary_search_left(log_times, end+1)
        print(end_index-start_index)
