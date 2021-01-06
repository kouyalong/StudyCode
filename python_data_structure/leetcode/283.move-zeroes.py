

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)


s = Solution()
t = [0, 1, 0, 3, 12]
s.moveZeroes(t)
print(t)
