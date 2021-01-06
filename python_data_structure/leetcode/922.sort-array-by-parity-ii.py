
from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        length = len(A)
        reA = [0 for _ in range(length)]
        j, k = 0, 1
        for i in range(length):
            if A[i] % 2 == 0:
                reA[j] = A[i]
                j += 2
            else:
                reA[k] = A[i]
                k += 2
        return reA


s = Solution()
print(s.sortArrayByParityII([4, 2, 5, 7]))
