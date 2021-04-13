# -*- coding: utf-8 -*-


from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(string, path):
            if not string:
                res.append(path)
                return
            for i in range(1, len(string)+1):
                if string[:i] == string[:i][::-1]:
                    dfs(string[i:], path+[string[:i]])

        dfs(s, [])
        return res


s = Solution()
print(s.partition("abccbaghhg"))
