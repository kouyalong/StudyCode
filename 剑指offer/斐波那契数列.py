# -*- coding: utf-8 -*-


class Solution:

    def Fibonacci(self, n):
        a, b = 0, 1
        while n > 1:
            a, b = b, a + b
            n -= 1
        return b

s = Solution()
ret = s.Fibonacci(3)
