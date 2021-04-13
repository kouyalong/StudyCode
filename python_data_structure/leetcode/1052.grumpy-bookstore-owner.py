# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        base = 0
        for i, g in enumerate(grumpy):
            if g == 0:
                base += customers[i]

        length = len(customers)
        max_increase = increase = sum(c * g for c, g in zip(customers[:X], grumpy[:X]))
        for i in range(X, length):
            increase += customers[i] * grumpy[i] - customers[i-X] * grumpy[i-X]
            max_increase = max(max_increase, increase)
        return base + max_increase


cc = [1, 0, 1, 2, 1, 1, 7, 5]
gg = [0, 1, 0, 1, 0, 1, 0, 1]
xx = 3
s = Solution()
print(s.maxSatisfied(cc, gg, xx))
