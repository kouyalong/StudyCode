# coding: utf-8


from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        nodes = [root]
        is_left_start = True
        result = list()
        while nodes:
            length = len(nodes)
            stuff_values = list()
            for i in range(length):
                node = nodes.pop(0)

                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)

                if is_left_start:
                    stuff_values.append(node.val)
                else:
                    stuff_values.insert(0, node.val)
            result.append(stuff_values)
            is_left_start = not is_left_start
        return result


s = Solution()
# [3,9,20,null,null,15,7]
# [1,2,3,4,null,null,5]
rt = TreeNode(1, left=TreeNode(2, left=TreeNode(4)), right=TreeNode(3,  right=TreeNode(5)))
print(s.zigzagLevelOrder(rt))
