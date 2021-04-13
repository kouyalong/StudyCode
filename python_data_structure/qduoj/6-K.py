# -*- coding: utf-8 -*-


def to_int(line: str):
    return [int(_n) for _n in line.split(" ")]


group_num = input()
for _ in range(int(group_num)):
    nums = to_int(input())
    client_num, people_num = nums[0], nums[1]
    client_issue_need = to_int(input())
    client_issue_need.sort()
    people_power = to_int(input())
    people_power.sort()
    k, j, match = 0, 0, 0
    while k < len(client_issue_need) and j < len(people_power):
        if people_power[j] >= client_issue_need[k]:
            match += 1
            j += 1
            k += 1
        else:
            j += 1
    print(match)
