# coding: utf-8


class Solution503:
    def nextGreaterElement(self, nums1, nums2):
        """
        https://leetcode-cn.com/problems/next-greater-element-i/?
        """
        dic = {}

        for i in range(len(nums2)):
            j = i + 1
            while j < len(nums2) and nums2[i] >= nums2[j]:
                j += 1
            if j < len(nums2) and nums2[i] < nums2[j]:
                dic[nums2[i]] = nums2[j]
        return [dic.get(x, -1) for x in nums1]
