# -*- coding: utf-8 -*-

from collections import defaultdict


it = input()


def to_int(line: str):
    return [int(_n) for _n in line.split(" ")]


pro_sum = to_int(it)[0]
while pro_sum > 0:
    try:
        nums_count = to_int(input())
        nums = to_int(input())
        count = 0
        n2c = defaultdict(int)
        n2c[1] = 0
        n2c[2] = 0
        for n in nums:
            n2c[n] += 1
        sorted_n2c = sorted(n2c.items(), key=lambda x: x[0], reverse=True)
        for k, _ in sorted_n2c:
            p = n2c[k]
            k_mod_3 = int(k % 3)
            if k_mod_3 == 0:
                count += p
            elif k_mod_3 == 2:
                if p <= n2c[1]:
                    count += p
                    n2c[1] -= p
                    n2c[k] -= p
                else:
                    count += n2c[1]
                    n2c[k] -= n2c[1]
                    n2c[1] = 0
            else:
                if n2c[2] >= p:
                    n2c[2] -= p
                    count += p
                else:
                    need_1_count = (p - n2c[2]) * 2
                    count += n2c[2]
                    n2c[2] = 0
                    if need_1_count <= n2c[1]:
                        count += need_1_count//2
                        n2c[1] -= need_1_count
                    else:
                        if n2c[1] % 2 == 1:
                            count += (n2c[1]-1)//2
                            n2c[1] = 1
                        else:
                            count += n2c[1]//2
                            n2c[1] = 0
        print(count)
    except:
        print(0)
    pro_sum -= 1
