# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ret = list()
        for i in range(len(S)):
            if S[i].isdigit():
                if ret:
                    ret = [item + S[i] for item in ret]
                else:
                    ret = [S[i]]
            else:
                new_ret = list()
                n = len(ret)
                for j in range(n):
                    new_ret.append(ret[j] + S[i].lower())
                    new_ret.append(ret[j] + S[i].upper())
                if not new_ret:
                    new_ret.append(S[i].lower())
                    new_ret.append(S[i].upper())
                ret = new_ret

        return ret


s = Solution()
ts = "a1b2"
print(s.letterCasePermutation(ts))
