# -*- coding: utf-8 -*-


from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodesCount = len(edges)
        parent = list(range(nodesCount + 1))

        def find(index: int) -> int:
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]

        def union(index1: int, index2: int):
            parent[find(index1)] = find(index2)

        for node1, node2 in edges:
            if find(node1) != find(node2):
                union(node1, node2)
                print(parent)
            else:
                return [node1, node2]
        return []


s = Solution()
ret = s.findRedundantConnection([[1, 2], [1, 3], [2, 4], [2, 5], [4, 5]])
print(ret)
