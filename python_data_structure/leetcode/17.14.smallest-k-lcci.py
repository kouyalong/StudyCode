# -*- coding: utf-8 -*-


from typing import List


class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        self.selected(arr, 0, len(arr) - 1, k)
        return arr[:k]

    def keil_split(self, arr, left, right):
        target = arr[right]
        pos = left - 1
        for i in range(left, right):
            if target >= arr[i]:
                pos += 1
                arr[i], arr[pos] = arr[pos], arr[i]
        arr[pos+1], arr[right] = arr[right], arr[pos+1]
        return pos + 1

    def selected(self, arr, left, right, k):
        pos = self.keil_split(arr, left, right)
        num = pos - left + 1
        # print(left, pos, num, "ppppp")

        if k < num:
            self.selected(arr, left, pos - 1, k),
        elif k > num:
            self.selected(arr, pos + 1, right, k - num)


s = Solution()
rtt = s.smallestK([1, 3, 5, 7, 2, 4, 6, 8], 4)
print(rtt)
