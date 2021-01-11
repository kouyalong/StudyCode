# coding: utf-8

from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n+1):
            divisible_by_3 = (i % 3 == 0)
            divisible_by_5 = (i % 5 == 0)
            num2str = ""
            if divisible_by_3:
                num2str += "Fizz"
            if divisible_by_5:
                num2str += "Buzz"
            if num2str:
                result.append(num2str)
            else:
                result.append(str(i))
        return result


s = Solution()
print(s.fizzBuzz(15))
