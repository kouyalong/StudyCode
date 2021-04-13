# -*- coding: utf-8 -*-


class Solution:

    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if len(s) * k == 0:
            return 0

        char_right_loc = dict()
        left = right = 0
        max_len = 1
        while right < len(s):
            char_right_loc[s[right]] = right
            right += 1
            del_index = min(char_right_loc.values())
            if len(char_right_loc.keys()) == k + 1:
                char_right_loc.pop(s[del_index])
                left = del_index + 1
            max_len = max(max_len, right-left)
        return max_len


string = "eceba"
k_num = 3
s = Solution()
print(s.lengthOfLongestSubstringKDistinct(string, k_num))
