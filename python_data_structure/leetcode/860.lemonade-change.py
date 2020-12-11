# coding: utf-8

from collections import defaultdict
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill2count = defaultdict(int)
        for _bill in bills:
            need_back = _bill - 5
            while need_back != 0:
                if bill2count[need_back]:
                    bill2count[need_back] -= 1
                    need_back = 0
                else:
                    if bill2count[5] > 0:
                        bill2count[5] -= 1
                    else:
                        return False
                    need_back -= 5
            bill2count[_bill] += 1
        return True


s = Solution()
print(s.lemonadeChange([5, 5, 10, 10, 20]))
