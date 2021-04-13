# -*- coding: utf-8 -*-


def to_int(line: str):
    return [int(_n) for _n in line.split(" ")]


def find_min_index(array: list):
    m = array[0]
    index = 0
    for i, n in enumerate(array):
        if n < m:
            index = i
    return index


def main():
    n_and_m = input().split(" ")
    n, m = int(n_and_m[0]), int(n_and_m[1])
    if not m:
        return -1
    need_times = to_int(input())
    if len(need_times) != n:
        return -1
    if not need_times:
        return -1
    speed_time = [0 for _ in range(m)]
    for i in range(n):
        index = find_min_index(speed_time)
        speed_time[index] += need_times[i]
    return min(speed_time) + 1


print(main())
