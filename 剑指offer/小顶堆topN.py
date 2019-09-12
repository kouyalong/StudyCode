# -*- coding: utf-8 -*-


class TopNHeap:
    # 先使用data前M个数，构建M长度的小顶堆，然后继续遍历data中的数记做data[i]
    # 如果data[i]小于data[0](小顶堆root)，则跳过data[i]，继续下一个data[i+1]
    # 一直到遍历完data

    def parent(self, n):
        # 父节点index
        return (n-1)//2

    def left(self, n):
        # 左儿子节点
        return 2*n+1

    def right(self, n):
        # 右儿子节点
        return 2*n+2

    def build(self, n, data):
        # 构建小顶堆
        for i in range(1, n):
            while i != 0 and data[self.parent(i)] > data[i]:
                data[i], data[self.parent(i)] = data[self.parent(i)], data[i]
                i = self.parent(i)

    def adjust(self, i, n, data):
        # 如果data[i] 小于小顶堆的顶data[0], 则不调整小顶堆
        if data[i] <= data[0]:
            return

        # 利用data[i], 调整小顶堆data[:n]
        data[i], data[0] = data[0], data[i]
        t = 0
        while (self.left(t) < n and data[t] > data[self.left(t)]) \
                | (self.right(t) < n and data[t] > data[self.right(t)]):
            if self.right(t) < n and data[self.right(t)] < data[self.left(t)]:
                # 如果右节点小于左节点，调整右节点
                data[t], data[self.right(t)] = data[self.right(t)], data[t]
                t = self.right(t)
            else:
                data[t], data[self.left(t)] = data[self.left(t)], data[t]
                t = self.left(t)

    def find(self, n, data):
        self.build(n, data)
        for i in range(n, len(data)):
            self.adjust(i, n, data)

        print(data)

tp = TopNHeap()
tp.find(10, [188, 321, 112, 34, 212, 323, 12, 34, 45, 656, 4323, 21,
            32, 657, 3434, 56678, 78, 2323, 39849, 99, 33, 444, 56,
             678, 67, 7893, 2333, 1214, 452, 133, 244, 133, 422, 61])

