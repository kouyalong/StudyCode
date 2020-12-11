# coding: utf-8


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/
class Solution117:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        nodes = [root]
        n, m = 1, 0
        while nodes:
            p = nodes.pop(0)
            if p.left:
                nodes.append(p.left)
                m += 1
            if p.right:
                nodes.append(p.right)
                m += 1
            n -= 1
            if n == 0:
                p.next = None
                n = m
                m = 0
            else:
                p.next = nodes[0]
        return root

