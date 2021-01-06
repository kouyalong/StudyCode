
from typing import List


class Solution:

    def mid_search(self, num, nums, is_max):
        first = 0
        last = len(nums) - 1
        while first < last:
            mid = (first + last + is_max) // 2
            if nums[mid] < num:
                first = mid + 1
            elif nums[mid] > num:
                last = mid - 1
            else:
                if is_max:
                    first = mid
                else:
                    last = mid
        return first

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        min_index = self.mid_search(target, nums, is_max=0)
        if nums[min_index] != target:
            return [-1, -1]

        max_index = self.mid_search(target, nums, is_max=1)
        return [min_index, max_index]

    def searchRange2(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        if size == 0:
            return [-1, -1]

        first_position = self.__find_first_position(nums, size, target)
        if first_position == -1:
            return [-1, -1]
        last_position = self.__find_last_position(nums, size, target)
        return [first_position, last_position]

    def __find_first_position(self, nums, size, target):
        left = 0
        right = size - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                right = mid
            else:
                # nums[mid] > target
                right = mid - 1

        if nums[left] == target:
            return left
        else:
            return -1

    def __find_last_position(self, nums, size, target):
        left = 0
        right = size - 1
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                left = mid
            else:
                # nums[mid] < target
                left = mid + 1

        # 由于能走到这里，说明在数组中一定找得到目标元素，因此这里不用再做一次判断
        return left


s = Solution()
print(s.searchRange([1, 2, 2, 3, 4, 5, 7], 2))
