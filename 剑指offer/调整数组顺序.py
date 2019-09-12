# -*- coding: utf-8 -*-


class Solution:

    def is_odd(self, number):
        return False if number % 2 == 0 else True

    def reOrderArray(self, array):
        index, count = 0, 0
        while count < len(array):
            count += 1
            if self.is_odd(array[index]):
                index += 1
                continue
            else:
                array.append(array.pop(index))
        return array

s = Solution()
ret = s.reOrderArray([2, 4, 6, 1, 3, 5, 7])
print(ret)
