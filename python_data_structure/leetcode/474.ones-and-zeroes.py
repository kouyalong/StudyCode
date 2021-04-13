# -*- coding: utf-8 -*-


from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(m+1)]
        for _s in strs:
            zero_count, one_count = 0, 0
            for zc in _s:
                if zc == "0":
                    zero_count += 1
                elif zc == "1":
                    one_count += 1
            for i in range(m, zero_count-1, -1):
                for j in range(n, one_count-1, -1):
                    dp[i][j] = max(dp[i][j], 1+dp[i-zero_count][j-one_count])
        return dp[m][n]


s = Solution()
print(s.findMaxForm(
    strs=["10", "0001", "111001", "1", "0"],
    m=5,
    n=3
))
