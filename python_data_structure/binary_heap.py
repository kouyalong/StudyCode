#!/usr/bin/python
# coding: utf-8


class BinaryHeap(object):
    # 二叉堆

    def __init__(self):
        self.heap_list = [0]
        self.heap_size = 0

    def pre_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i//2]:
                self.heap_list[i], self.heap_list[i//2] = self.heap_list[i//2], self.heap_list[i]
            i //= 2

    def insert(self, key):
        self.heap_list.append(key)
        self.heap_size += 1
        self.pre_up(self.heap_size)

    def mid_child(self, i):
        double_i = 2*i
        if double_i + 1 > self.heap_size:
            return double_i
        else:
            if self.heap_list[double_i] < self.heap_list[double_i+1]:
                return double_i
            else:
                return double_i + 1

    def pre_down(self, i):
        while (i * 2) <= self.heap_size:
            mc = self.mid_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc

    def find_min(self):
        pass

    def del_min(self):
        retval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.heap_size]
        self.heap_size -= 1
        self.heap_list.pop()
        self.pre_down(1)
        return retval

    def size(self):
        pass

    def create(self, al):
        i = len(al) // 2
        self.heap_size = len(al)
        self.heap_list = [0] + al
        while i > 0:
            self.pre_down(i)
            i -= 1


def main_binary_heap():
    hp = BinaryHeap()
    hp.create([9, 5, 6, 2, 3])
    print(hp.heap_list)
    print(hp.del_min())
    print(hp.del_min())
    print(hp.del_min())
    print(hp.del_min())
    print(hp.del_min())


class CompleteBinaryTree(object):

    def __init__(self, ):
        pass
