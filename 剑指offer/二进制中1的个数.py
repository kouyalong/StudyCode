# -*- coding: utf-8 -*-


class Solution:

    def NumberOf1(self, n):
        count = 0
        if n < 0:
            n &= 0xffffffff
        while n:
            count += 1
            n &= (n - 1)
        print(count)
        return count


s = Solution()
s.NumberOf1(-4)