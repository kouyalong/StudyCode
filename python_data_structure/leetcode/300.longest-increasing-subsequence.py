# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            """我前面比我小的值有多少个"""
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


s = Solution()
print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18, 19, 20]))
