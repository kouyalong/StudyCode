# -*- coding: utf-8 -*-

class Solution:

    def jumpFloorII(self, n):
        return 2 ** (n - 1)

s = Solution()
ret = s.jumpFloorII(3)
