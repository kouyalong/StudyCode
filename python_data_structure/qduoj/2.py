# -*- coding: utf-8 -*-


lines = input().split("\n")
pro_sum = int(lines[0])


def to_int(line: str):
    return [int(_n) for _n in line.split(" ")]


def pick_link(link, reaches):
    nt = 1
    count = 0
    while nt or reaches:
        un = link.setdefault

    if not reaches:
        return count
    else:
        return -1


result = []
index = 1
for i in range(pro_sum):
    n_p = to_int(lines[index])
    n, p = n_p[0], n_p[1]
    reaches = to_int(lines[index+1])
    default_i = index + 2
    sides = to_int(lines[default_i])[0]

    link = dict()
    for _side in range(default_i+1, default_i+1+sides):
        points = to_int(lines[_side])
        link.setdefault(points[0], []).append(points[1])


    result.append()
