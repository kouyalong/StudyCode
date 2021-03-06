# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre:
            return None
        elif len(pre) == 1:
            return TreeNode(pre[0])
        else:
            root = TreeNode(pre[0])
            pos = tin.index(pre[0])
            root.left = self.reConstructBinaryTree(pre[1:pos+1], tin[:pos])
            root.right = self.reConstructBinaryTree(pre[pos+1:], tin[pos+1:])
            return root


s = Solution()
r = s.reConstructBinaryTree(
    [1, 2, 4, 7, 3, 5, 6, 8],
    [4, 7, 2, 1, 5, 3, 8, 6]
)


def inOrder(rr):
    if rr:
        print(rr.val)
        inOrder(rr.left)
        inOrder(rr.right)

inOrder(r)
