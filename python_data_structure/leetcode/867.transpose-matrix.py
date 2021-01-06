

from typing import List


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        if not A:
            return A

        length, wight = len(A), len(A[0])
        new_list = [[0 for _ in range(length)] for _ in range(wight)]
        for i in range(length):
            for j in range(wight):
                new_list[j][i] = A[i][j]
        return new_list


s = Solution()
print(s.transpose([[1, 2, 3], [4, 5, 6]]))
