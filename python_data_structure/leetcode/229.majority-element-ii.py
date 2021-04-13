# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def _judge_num_count(self, nums, num):
        count = 0
        for n in nums:
            if n == num:
                count += 1
                if count > len(nums) // 3:
                    return True
        if count > len(nums) // 3:
            return True
        else:
            return False

    def majorityElement(self, nums: List[int]) -> List[int]:
        c1, c2, num1, num2 = 0, 0, None, None
        for n in nums:
            if num1 == n:
                c1 += 1
                continue
            if num2 == n:
                c2 += 1
                continue
            if c1 == 0:
                num1 = n
                c1 += 1
                continue
            if c2 == 0:
                num2 = n
                c2 += 1
                continue

            c1 -= 1
            c2 -= 1

        res = []
        if c1 != 0 and self._judge_num_count(nums, num1):
            res.append(num1)

        if c2 != 0 and self._judge_num_count(nums, num2):
            res.append(num2)
        return res


s = Solution()
print(s.majorityElement([1, 1, 1, 3, 3, 2, 2, 2]))
