# coding: utf-8

import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = collections.deque()
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
        ans = [nums[q[0]]]
        for i in range(k, n):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            while q[0] <= i - k:
                q.popleft()
            ans.append(nums[q[0]])

        return ans

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:

        # 保存 nums[i-k:i]之间 存在的单调递减的一个子数组 的index
        desc_number_index = list()
        result = list()
        for i in range(k):
            # 如果当前的num大于 单调递减的数组的第一个，那么清空当前 单调递减数组
            while desc_number_index and nums[i] >= nums[desc_number_index[-1]]:
                desc_number_index.pop(-1)
            desc_number_index.append(i)
        result.append(nums[desc_number_index[0]])
        print(desc_number_index)
        for i in range(k, len(nums)):
            # 动态维护 单调递减数组
            while desc_number_index and nums[i] >= nums[desc_number_index[-1]]:
                desc_number_index.pop(-1)
            desc_number_index.append(i)
            print(desc_number_index)
            # 维护单调递减数组在 滑动窗口k的范围内
            while desc_number_index[0] <= i-k:
                desc_number_index.pop(0)
            result.append(nums[desc_number_index[0]])
        return result


ns = [1,3,1,2,0,5]
k = 3
s = Solution()
print(s.maxSlidingWindow2(ns, k))
