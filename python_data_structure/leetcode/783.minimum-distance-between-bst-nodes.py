# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.min_diff = 0xffffffff
        self.local_value = None
        self.pre_order(root)
        return self.min_diff

    def pre_order(self, root):
        if root:
            self.pre_order(root.left)
            if not self.local_value:
                self.local_value = root.val
            else:
                diff = root.val - self.local_value
                self.min_diff = self.min_diff if self.min_diff <= diff else diff
                self.local_value = root.val
            self.pre_order(root.right)


s = Solution()
rt = TreeNode(90, left=TreeNode(69, left=TreeNode(49, right=TreeNode(52)), right=TreeNode(89)))
print(s.minDiffInBST(rt))
