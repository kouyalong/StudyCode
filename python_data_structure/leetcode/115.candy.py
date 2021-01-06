# coding: utf-8


from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        length = len(ratings)
        left = [0] * length

        for i in range(length):
            if i > 0 and ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
            else:
                left[i] = 1

        right = ret = 0
        for i in range(length - 1, -1, -1):
            if i < length - 1 and ratings[i] > ratings[i + 1]:
                right += 1
            else:
                right = 1
            ret += max(left[i], right)
        return ret


s = Solution()
print(s.candy([1, 2, 2]))


class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1

        repeat_chars = set()
        s = list(s)
        n = len(s)
        for i in range(n):
            flag = False
            if s[i] in repeat_chars:
                continue
            for j in range(i+1, n):
                if str(s[i]) == str(s[j]):
                    flag = True
                    repeat_chars.add(s[i])
                    break
            if not flag:
                return i
        return -1

s = Solution()
print(s.firstUniqChar("cc"))

