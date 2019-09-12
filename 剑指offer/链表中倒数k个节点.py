# -*- coding: utf-8 -*-


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def FindKthToTail(self, head, k):
        ### 滑动窗口
        if not head or not k:
            return None
        first, last = head, head
        for i in range(k-1):
            if first.next:
                first = first.next
            else:
                return None
        while first.next:
            last = last.next
            first = first.next
        return last

