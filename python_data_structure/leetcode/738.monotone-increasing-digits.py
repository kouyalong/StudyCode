# coding: utf-8


class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        numbers = []
        num = N
        while num:
            d = num % 10
            numbers.insert(0, d)
            num = num // 10

        idx = -1
        length = len(numbers)
        for i in range(length-1):
            if numbers[i] > numbers[i+1]:
                idx = i
                break

        while idx != -1:
            numbers[idx] -= 1
            for i in range(idx+1, length):
                numbers[i] = 9

            idx = -1
            for i in range(length - 1):
                if numbers[i] > numbers[i + 1]:
                    idx = i
                    break

        return int("".join([str(n) for n in numbers]))


s = Solution()
print(s.monotoneIncreasingDigits(10))
