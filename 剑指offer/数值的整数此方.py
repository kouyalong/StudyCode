# -*- coding: utf-8 -*-


class Solution:

    def Power(self, base, exponent):
        if base == 0 and exponent < 0:
            return 0
        abs_exponent = abs(exponent)

        ret = self.PowerFunc(base, abs_exponent)

        if exponent < 0:
            ret = 1 / ret
        return ret

    def PowerFunc(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        ret = self.PowerFunc(base, exponent >> 1)
        ret *= ret

        if exponent & 1 == 1:
            ret *= base
        return ret


s = Solution()
r = s.Power(2, 100)
print(r)