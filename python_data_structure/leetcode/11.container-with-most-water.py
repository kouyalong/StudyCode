# coding: utf-8

from typing import List


class Solution:
    """
    area[i, j] = min(height[i], height[j]) * (j - i)
    f(i, j) =
    """

    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


s = Solution()
print(s.maxArea([1, 2, 1]))
