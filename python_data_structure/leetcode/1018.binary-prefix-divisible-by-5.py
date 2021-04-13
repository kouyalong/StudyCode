# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        ans = list()
        prefix = 0
        for num in A:
            prefix = ((prefix << 1) + num) % 5
            ans.append(prefix == 0)
        return ans


s = Solution()
print(s.prefixesDivBy5([0, 1, 1, 1, 1]))
