# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        result = list()
        for interval in intervals:
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        return result

    # def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    #     parent = [i for i in range(len(intervals))]
    #
    #     def find(index):
    #         if index != parent[index]:
    #             parent[index] = find(parent[index])
    #         return parent[index]
    #
    #     def union(index1, index2):
    #         parent[find(index1)] = find(index2)
    #


s = Solution()
ll = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(s.merge(ll))
