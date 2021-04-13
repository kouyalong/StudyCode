# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        ret = [0, 1]
        if num <= 1:
            return ret[:num+1]

        flag = 1
        for i in range(2, num+1):
            if (flag << 1) == i:
                flag = flag << 1
                ret.append(1)
            else:
                ret.append(ret[flag] + ret[i-flag])
        return ret

"""
0 1 1 2 1 2 2 3 1 2 2  3  2  3  3  4
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
"""
number = 5
s = Solution()
print(s.countBits(number))
