# coding: utf-8


class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0x100000000
        MAX_INT = 0x7FFFFFFF
        MIN_INT = MAX_INT + 1
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) % MASK
            b = carry % MASK
        return a if a <= MAX_INT else ~(~(a % MIN_INT) ^ MAX_INT)

    def getSum2(self, a: int, b: int) -> int:
        a &= 0xFFFFFFFF
        b &= 0xFFFFFFFF
        while b:
            carry = a & b
            a ^= b
            b = ((carry) << 1) & 0xFFFFFFFF
            # print((a, b))
        return a if a < 0x80000000 else ~(a^0xFFFFFFFF)
