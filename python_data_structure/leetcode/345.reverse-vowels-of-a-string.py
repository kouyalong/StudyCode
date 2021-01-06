# coding: utf-8


class Solution:
    def reverseVowels(self, s: str) -> str:
        i, j = 0, len(s)-1
        s = list(s)
        vowels = ["a", "o", "e", "i", "u", "A", "O", "E", "I", "U"]
        while i <= j:
            if s[i] in vowels and s[j] in vowels:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            else:
                if s[i] not in vowels:
                    i += 1
                if s[j] not in vowels:
                    j -= 1
        return "".join(s)


sl = Solution()
print(sl.reverseVowels(".a"))
