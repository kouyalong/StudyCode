# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        n, m = len(matrix), len(matrix[0])
        i, j = 0, m - 1
        while i <= n-1 and j >= 0:
            p = matrix[i][j]
            if target > p:
                i += 1
            elif target < p:
                j -= 1
            else:
                return True
        return False


s = Solution()
mt = [[1, 4, 7, 11, 15],
      [2, 5, 8, 12, 19],
      [3, 6, 9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]]
tg = 18
print(s.searchMatrix(mt, tg))
