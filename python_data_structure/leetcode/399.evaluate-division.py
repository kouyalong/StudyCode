# coding: utf-8、

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

    def merge(self, x, y):
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


class UnionValueFind:
    def __init__(self):
        """
        记录每个节点的父节点
        记录每个节点到根节点的权重
        """
        self.father = {}
        self.value = {}

    def find(self, x):
        """
        查找根节点
        路径压缩
        更新权重
        """
        root = x
        # 节点更新权重的时候要放大的倍数
        base = 1
        while self.father[root] is not None:
            root = self.father[root]
            base *= self.value[root]

        while x != root:
            original_father = self.father[x]
            # 离根节点越远，放大的倍数越高
            self.value[x] *= base
            base /= self.value[original_father]
            #
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
            # 四边形法则更新根节点的权重
            self.value[root_x] = self.value[y] * val / self.value[x]

    def is_connected(self, x, y):
        """
        两节点是否相连
        """
        return x in self.value and y in self.value and self.find(x) == self.find(y)

    def add(self, x):
        """
        添加新节点，初始化权重为1.0
        """
        if x not in self.father:
            self.father[x] = None
            self.value[x] = 1.0


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        uvf = UnionValueFind()
        for (a, b), val in zip(equations, values):
            uvf.add(a)
            uvf.add(b)
            uvf.merge(a, b, val)

        res = [-1.0] * len(queries)

        for i, (a, b) in enumerate(queries):
            if uvf.is_connected(a, b):
                res[i] = uvf.value[a] / uvf.value[b]
        return res


s = Solution()
eq = [["a", "b"], ["b", "c"]]
vs = [2.0, 3.0]
qs = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
print(s.calcEquation(eq, vs, qs))
