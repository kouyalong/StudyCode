# coding: utf-8


class Solution:
    def calculate(self, s: str) -> int:
        _items = list()
        _number_string = ""
        s += "+"
        for item in s:
            if item == " ":
                continue
            elif item in ["+", "-", "*", "/"]:
                _items.append(int(_number_string))
                _number_string = ""

                if len(_items) >= 3 and _items[-2] in ["*", "/"]:
                    _items.append(self._calculate(_items))

                if item in ["+", "-"]:
                    while len(_items) >= 3:
                        _items.append(self._calculate(_items))
                _items.append(item)
            else:
                _number_string += item
        return _items[0]

    def _calculate(self, items):
        b = items.pop()
        flag = items.pop()
        a = items.pop()
        if flag == "+":
            return a + b
        elif flag == "-":
            return a - b
        elif flag == "*":
            return a * b
        else:
            return a // b


s = Solution()
print(s.calculate("14/3*2"))
print(eval("13+2*12-12/6-1-4+5"))
