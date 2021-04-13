# -*- coding: utf-8 -*-

from typing import List
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = list(map(str, nums))
        compare = lambda x, y: -1 if x+y > y+x else 1
        nums_str.sort(key=cmp_to_key(compare))
        ret = "".join(nums_str)
        if ret[0] == "0":
            return "0"
        return ret


s = Solution()
print(s.largestNumber([3, 32, 34, 5, 9]))
