# coding: utf-8

from typing import List


class Solution:
    """
    f(n) = min(f(n-1)+cost[n-1], f(n-2)+cost[n-2])
    """
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        dp = [0] * (length+1)
        for i in range(2, length+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return dp[length]

    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            cost[i] = min(cost[i - 2], cost[i - 1]) + cost[i]
        return min(cost[-2], cost[-1])


s = Solution()
arg_list = [1, 100, 101, 102, 1, 100, 1, 1, 100, 1]
ret = s.minCostClimbingStairs(arg_list)
ret2 = s.minCostClimbingStairs2(arg_list)
print(ret)
print(ret2)


class Solution111:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        s = s.lower()
        while left <= right:
            if not s[left] or not str(s[left]).isalnum():
                left += 1
                continue
            if not s[right] or not str(s[right]).isalnum():
                right -= 1
                continue

            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True


s = Solution111()
print(s.isPalindrome("race a car"))
