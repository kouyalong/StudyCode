# coding: utf-8


class Solution:
    def _nump(self, n):
        p = 0
        while n > 0:
            p += (n % 10) ** 2
            n = n // 10
        return p

    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n * n
        while fast != slow:
            slow = self._nump(slow)
            fast = self._nump(self._nump(fast))
        return fast == 1


s = Solution()
print(s.isHappy(119))

"""
0   1   2   3   4   5   6   7   8   9

0   1   4   9   16  25  36  49  64  81
0   1   16  81  37  29  45  97  52  65
0   1   37  65  58  85  41  130 29  61
0   1   58  61  89  89  17  10  85  37
0   1   89  37  156 156 50  1   89  58
0   1   156 58  62  62  25  1   145 89
0   1   62  89  40  40  29  1   42  145
0   1   40  145 16  16  85  1   20  42
0   1   16  42  37  37  89  1   4   20
0   1   37  20  58  58  145 1   16  4
0   1   58  4   89  89  42  1   37  16
0   1   89  16  156 156 20  1   58  37
"""
