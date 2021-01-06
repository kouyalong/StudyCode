# coding: utf-8

from typing import List


def two_sum(array, target):
    value2index = dict()

    for i in range(len(array)):
        diff = target - array[i]
        if value2index.get(diff) is not None:
            return [value2index[diff], i]
        value2index[array[i]] = i
    return []


ret = two_sum([2, 7, 11, 15], 9)
print(ret)


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        for i in range(length - 1):
            diff = target - numbers[i]
            left = i + 1
            right = length - 1
            mid = (left + right) // 2
            flag = False
            while left <= right:
                if numbers[mid] < diff:
                    left = mid + 1
                elif numbers[mid] > diff:
                    right = mid - 1
                else:
                    flag = True
                    break
                mid = (left + right) // 2
            if flag:
                return [i + 1, mid + 1]

    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        if length < 2:
            return []

        left = 0
        right = length - 1
        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left + 1, right + 1]
        return []


s = Solution()
print(s.twoSum([2, 3, 4], 6))
print(s.twoSum2([1, 2, 7, 9, 11, 15], 9))
