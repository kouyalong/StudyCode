# coding: utf-8

from collections import Counter
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        set_s_and_length = dict()
        for s in strs:
            set_s = list(set(s))
            set_s.sort()
            cs = Counter(list(s))
            cs_str = "".join([str(_s)+str(cs.get(_s, 0)) for _s in set_s])
            set_s_and_length.setdefault(
                ("".join(set_s), len(s), cs_str), []
            ).append(s)
        return list(set_s_and_length.values())


pp = Solution()
print(pp.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
