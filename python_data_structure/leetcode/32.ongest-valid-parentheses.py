

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stek = [-1]
        length = len(s)
        result = 0
        for i in range(length):
            if len(stek) == 1:
                stek.append(i)
            else:
                top = s[stek[-1]]
                if top == "(" and s[i] == ")":
                    stek.pop()
                    result = max(i-stek[-1], result)
                else:
                    stek.append(i)
        return result


s = Solution()
print(s.longestValidParentheses("()()()()(((())))))((()()()()()()()()()"))
