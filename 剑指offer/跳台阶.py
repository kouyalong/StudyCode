# -*- coding: utf-8 -*-

class Solution:

    def jumpFloor(self, n):
        a, b = 1, 1
        while n > 1:
            a, b = b, a + b
            n -= 1
        return b

s = Solution()
ret = s.jumpFloor(4)
