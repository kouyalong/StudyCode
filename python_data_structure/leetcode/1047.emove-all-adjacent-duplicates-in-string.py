# -*- coding: utf-8 -*-


class Solution:
    def removeDuplicates(self, S: str) -> str:
        ret = ""
        for ss in S:
            if not ret:
                ret = ss
                continue
            if ret[-1] == ss:
                ret = ret[:-1]
            else:
                ret += ss
        return ret


s = Solution()
print(s.removeDuplicates("abbaca"))
