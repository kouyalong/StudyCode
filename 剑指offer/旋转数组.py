# -*- coding: utf-8 -*-


class Solution:

    def minNumberInRotateArray(self, rotateArray):
        ### 二分查找
        if len(rotateArray) == 0:
            return 0
        mid, left, right = 0, 0, len(rotateArray) - 1
        while rotateArray[left] >= rotateArray[right]:
            if right - left == 1:
                mid = right
                break
            mid = (left + right) // 2
            if rotateArray[left] == rotateArray[mid] and rotateArray[mid] == rotateArray[right]:
                return self.minInorder(rotateArray, left, right)
            if rotateArray[mid] >= rotateArray[left]:
                left = mid
            else:
                right = mid
        return rotateArray[mid]

    def minInorder(self, array, left, right):
        result = array[left]
        for i in range(left + 1, right + 1):
            if array[i] < result:
                result = array[i]
        return result


s = Solution()
ret = s.minNumberInRotateArray([1, 1, 1, 0, 1])
print(ret)
