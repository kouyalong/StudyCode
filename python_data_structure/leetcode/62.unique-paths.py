# coding: utf-8


class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[m - 1][n - 1]

    def do(self, m, n):
        if m == 1 and n == 1:
            return 0
        if m == 1 or n == 1:
            return 1
        left_key = (m-1, n)
        right_key = (m, n-1)
        left = self.cache.get(left_key)
        if not left:
            left = self.cache[(m-1, n)] = self.do(m-1, n)
        right = self.cache.get(right_key)
        if not right:
            right = self.cache[(m, n-1)] = self.do(m, n-1)
        return left + right

    def uniquePaths2(self, m: int, n: int) -> int:
        self.cache = dict()
        return self.do(m, n)


s = Solution()
print(s.uniquePaths(100, 100))
print(s.uniquePaths2(100, 100))
