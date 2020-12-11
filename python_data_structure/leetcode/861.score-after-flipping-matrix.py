# coding: utf-8


class Solution:
    def matrixScore(self, A: list) -> int:
        if not A:
            return 0

        m, n = len(A), len(A[0])
        for i in range(m):
            if A[i][0] == 0:
                for k in range(n):
                    A[i][k] = 0 if A[i][k] == 1 else 1
        result = 0
        for j in range(n):
            s = sum([A[p][j] for p in range(m)])
            result += max(s, m-s) * (1 << (n-j-1))
        return result


s = Solution()
print(s.matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]]))
