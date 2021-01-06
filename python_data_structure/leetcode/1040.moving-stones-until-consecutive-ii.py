# coding: utf-8

from typing import List


class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        n = len(stones)
        # 所有石子插到[0,-2]或者[1,-1]（第一次移动最后一个或者第一个）的最大长度的稀疏区间，这里面有更多的空位，一步步移动，最终缩到紧凑区间
        maxMove = max(stones[n - 1] - stones[1] - (n - 2), stones[n - 2] - stones[0] - (n - 2))
        minMove = n
        # 直接将所有石子往长度为n的紧凑区间插入
        l = 0
        for r in range(n):
            # 窗口范围大于n时，缩小窗口，保证窗口大小为n，因为总共只有n个石子
            while stones[r] - stones[l] + 1 > n:
                l += 1
            cnt = r - l + 1  # 窗口内石子数量
            # 特殊情形：窗口内有n-1个连续石子，窗口外有一个零散的石子，这时只能移动连续段的边界石子，需要2步完成
            if cnt == n - 1 and stones[r] - stones[l] + 1 == n - 1:
                minMove = min(minMove, 2)
            else:
                minMove = min(minMove, n - cnt)
        return [minMove, maxMove]


s = Solution()
print(s.numMovesStonesII([6, 5, 4, 3, 10]))
