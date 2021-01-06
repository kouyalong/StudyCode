# coding: utf-8

from collections import defaultdict
from typing import List


class Solution:

    def insert_list(self, items: List, num):
        if not items:
            return [num]
        flag = False
        length = len(items)
        for i in range(length):
            if num <= items[i]:
                items.insert(i, num)
                flag = True
                break
        if not flag:
            items.append(num)
        return items

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        item2count = defaultdict(int)
        not_in_arr2 = list()
        for item in arr1:
            item2count.setdefault(item, 0)
            item2count[item] += 1
            if item not in set(arr2):
                not_in_arr2 = self.insert_list(not_in_arr2, item)
        
        result = []
        for item in arr2:
            count = item2count.get(item)
            for _ in range(count):
                result.append(item)
            item2count.pop(item)
        result.extend(not_in_arr2)
        return result

    def relativeSortArray2(self, arr1: List[int], arr2: List[int]) -> List[int]:
        def mycmp(x: int):
            return rank[x] if x in rank else x
        
        n = len(arr2)
        rank = {x: i - n for i, x in enumerate(arr2)}
        print(rank)
        arr1.sort(key=mycmp)
        return arr1


s = Solution()
print(s.relativeSortArray2([2,3,1,3,2,4,6,7,9,2,19, 8, 10], [2,1,4,3,9,6]))
