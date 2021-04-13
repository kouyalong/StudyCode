# -*- coding: utf-8 -*-


class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.node_list = list()

    def pre_dfs(self, root: TreeNode):
        if root:
            self.node_list.append(root.val)
            self.pre_dfs(root.left)
            self.pre_dfs(root.right)

    def mid_dfs(self, root):
        if root:
            self.pre_dfs(root.left)
            self.node_list.append(root.val)
            self.pre_dfs(root.right)

    def last_dfs(self, root):
        if root:
            self.pre_dfs(root.left)
            self.pre_dfs(root.right)
            self.node_list.append(root.val)

    def bfs(self, root: TreeNode):
        q = [root]
        while q:
            length = len(q)
            for i in range(length):
                node = q.pop(0)
                self.node_list.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

    def pre_bfs(self, root: TreeNode):
        q = []
        while q or root:
            while root:
                self.node_list.append(root.val)
                q.append(root)
                root = root.left
            root = q.pop()
            root = root.right

    def mid_bfs(self, root):
        q = []
        while q or root:
            while root:
                q.append(root)
                root = root.left
            root = q.pop()
            self.node_list.append(root.val)
            root = root.right

    def post_bfs(self, root: TreeNode):
        q = [root]
        while q:
            node = q.pop()
            self.node_list.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        self.node_list = self.node_list[::-1]

    def post_dfs2(self, root: TreeNode):
        if not root:
            return []

        nodes = [root]
        result = list()
        while nodes:
            node = nodes[-1]
            if not node.left and not node.right:
                p = nodes.pop()
                result.append(p.val)
            else:
                if node.right:
                    nodes.append(node.right)
                    node.right = None
                if node.left:
                    nodes.append(node.left)
                    node.left = None
        return result


r = TreeNode(1,
             left=TreeNode(2, left=TreeNode(3), right=TreeNode(4)),
             right=TreeNode(5, left=TreeNode(6), right=TreeNode(7)))

s = Solution()
s.post_bfs(r)
print(s.node_list)
