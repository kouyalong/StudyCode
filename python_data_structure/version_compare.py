# -*- coding: utf-8 -*-


def compare(version1: str, version2: str):
    version1_nums = version1.split(sep=".")
    version2_numns = version2.split(sep=".")
    len1 = len(version1_nums)
    len2 = len(version2_numns)
    if len1 < len2:
        version1_nums.extend(['0'] * (len2- len1))
    else:
        version2_numns.extend(['0'] * (len1 - len2))
    for i in range(len1):
        v1 = int(version1_nums[i])
        v2 = int(version2_numns[i])
        if v2 == v1:
            continue
        elif v2 > v1:
            return version1
        else:
            return version2
    return version1


res = compare("1.0.0.1.1", "1.0.0.0.22")
print(res)
