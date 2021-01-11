# coding: utf-8

from math import gcd
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        for i in range(gcd(k, n)):
            current = i
            prev = nums[i]
            flag = True
            while i != current or flag:
                print(nums, prev)
                flag = False
                nt = ((current+k) % n)
                nums[nt], prev = prev, nums[nt]
                current = nt


def my_gcd1(a, b):
    if b == 0:
        return a
    return my_gcd1(b, a % b)


def my_gcd2(a, b):
    if a == b:
        return a
    elif a > b:
        a = a - b
    else:
        b = b - a
    return my_gcd2(a, b)


print(my_gcd2(3, 7))

n = [1, 2, 3, 4, 5, 6, 7]
s = Solution()
s.rotate(n, 3)
print(n)
