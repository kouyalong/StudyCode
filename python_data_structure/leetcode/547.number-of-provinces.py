# coding: utf-8

from typing import List


class UnionFind:
    def __init__(self):
        """
        记录每个节点的父节点
        """
        self.father = {}

    def find(self, x):
        """
        查找根节点
        路径压缩
        """
        root = x

        while self.father[root] is not None:
            root = self.father[root]

        # 路径压缩
        while x != root:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father

        return root

    def merge(self, x, y, val):
        """
        合并两个节点
        """
        root_x, root_y = self.find(x), self.find(y)

        if root_x != root_y:
            self.father[root_x] = root_y

    def is_connected(self, x, y):
        """
        判断两节点是否相连
        """
        return self.find(x) == self.find(y)

    def add(self, x):
        """
        添加新节点
        """
        if x not in self.father:
            self.father[x] = None


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i: int):
            for j in range(provinces):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)

        provinces = len(isConnected)
        visited = set()
        circles = 0

        for i in range(provinces):
            if i not in visited:
                dfs(i)
                circles += 1

        return circles


class UnionFind1:
    def __init__(self):
        self.father = {}
        # 额外记录集合的数量
        self.num_of_sets = 0

    def find(self, x):
        root = x
        while self.father[root] != None:
            root = self.father[root]

        while x != root:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father
        return root

    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)

        if root_x != root_y:
            self.father[root_x] = root_y
            # 集合的数量-1
            self.num_of_sets -= 1

    def add(self, x):
        if x not in self.father:
            self.father[x] = None
            # 集合的数量+1
            self.num_of_sets += 1


class Solution1:
    def findCircleNum(self, M: List[List[int]]) -> int:
        uf = UnionFind1()
        for i in range(len(M)):
            print(uf.father, "b")
            uf.add(i)
            for j in range(i):
                if M[i][j]:
                    print(i, j)
                    uf.merge(i, j)
            print(uf.father, "a")

        return uf.num_of_sets


ic = [[1,0,0,0,1,1,0,1,0,0,0,1,0,0,0],[0,1,0,0,1,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,1,0,0,0,0,0,0,0,1,1,0],[0,0,0,1,0,0,0,0,0,0,0,1,1,1,0],[1,1,1,0,1,0,0,0,0,0,1,0,0,0,0],[1,0,0,0,0,1,0,0,0,1,0,0,0,0,0],[0,1,0,0,0,0,1,0,1,0,0,0,0,0,0],[1,0,0,0,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,1,0,0,0,0,0,1],[0,0,0,0,0,1,0,0,0,1,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0,1,0,0,1,0],[1,0,0,1,0,0,0,0,0,0,0,1,1,0,0],[0,0,1,1,0,0,0,0,0,0,0,1,1,0,0],[0,0,1,1,0,0,0,0,0,0,1,0,0,1,0],[0,0,0,0,0,0,0,0,1,0,0,0,0,0,1]]
s = Solution1()
print(s.findCircleNum(ic))

