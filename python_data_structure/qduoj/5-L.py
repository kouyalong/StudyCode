# -*- coding: utf-8 -*-

from collections import defaultdict


def to_int(line: str):
    return [int(_n) for _n in line.split(" ")]


def binary_search_left(times: list, pt):
    left = 0
    right = len(times) - 1
    while left <= right:
        mid = left + (right - left)//2
        if pt >= times[mid]:
            left = mid + 1
        else:
            right = mid - 1
    if left == 0:
        return 0
    return left-1


def binary_search_right(times: list, pt):
    left = 0
    right = len(times) - 1
    while left <= right:
        mid = left + (right - left)//2
        if times[mid] < pt:
            left = mid + 1
        else:
            right = mid - 1
    if right == len(times)-1:
        return len(times)-1
    return right + 1


attack_type2time_and_count = defaultdict(lambda: defaultdict(list))
input_nums = to_int(input())
for i in range(input_nums[0]):
    attack_record = input().split(" ")
    attack_type2time_and_count[attack_record[1]]["time"].append(
        int(attack_record[0])
    )
    attack_type2time_and_count[attack_record[1]]["count"].append(
        int(attack_record[2])
    )

for i in range(input_nums[1]):
    search_info = input().split(" ")
    time_start, time_end = int(search_info[0]), int(search_info[1])
    search_attack_type = search_info[2]
    if not attack_type2time_and_count[search_attack_type]:
        print(0)
    else:
        index_start = binary_search_left(
            attack_type2time_and_count[search_attack_type]["time"],
            time_start - 1
        )
        index_end = binary_search_right(
            attack_type2time_and_count[search_attack_type]["time"],
            time_end + 1
        )
        record_count_list = attack_type2time_and_count[search_attack_type]["count"]
        count = sum(record_count_list[index_start+1: index_end])
        print(count)
