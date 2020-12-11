# coding: utf-8


import collections


class Solution:
    def isPossible(self, nums: list) -> bool:
        countMap = collections.Counter(nums)
        endMap = collections.Counter()

        for x in nums:
            count = countMap[x]
            if count > 0:
                prevEndCount = endMap.get(x - 1, 0)
                if prevEndCount > 0:
                    countMap[x] -= 1
                    endMap[x - 1] = prevEndCount - 1
                    endMap[x] += 1
                else:
                    count1 = countMap.get(x + 1, 0)
                    count2 = countMap.get(x + 2, 0)
                    if count1 > 0 and count2 > 0:
                        countMap[x] -= 1
                        countMap[x + 1] -= 1
                        countMap[x + 2] -= 1
                        endMap[x + 2] += 1
                    else:
                        return False
        return True

