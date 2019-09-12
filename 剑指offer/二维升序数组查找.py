# -*- coding: utf-8 -*-


class Solution:
    # array 二维列表
    def Find(self, target, array):
        ret = self.Search(target, array, 0, len(array[0])-1)
        print(ret)
        return True if ret else False

    def Search(self, target, array, row, col):
        if col < 0 or row > len(array)-1:
            return False
        if array[row][col] > target:
            return self.Search(target, array, row, col-1)
        elif array[row][col] < target:
            return self.Search(target, array, row+1, col)
        else:
            return row, col


s = Solution()
s.Find(7,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]])
