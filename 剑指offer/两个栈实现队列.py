# -*- coding: utf-8 -*-


class Solution:
    def __init__(self):
        self.stack1 = list()
        self.stack2 = list()

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


s = Solution()
print(s.push(1))
print(s.push(2))
print(s.push(3))
print(s.push(4))
print(s.pop())
print(s.push(5))
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
