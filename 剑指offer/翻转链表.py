# -*- coding: utf-8 -*-


class ListNode:
    def __init__(self, x, n=None):
        self.val = x
        self.next = n


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, ln):
        if not ln:
            return ln
        last = None
        while ln:
            tmp = ln.next
            ln.next = last
            last = ln
            ln = tmp
        return last


    def ReverseList(self, pHead):
        # write code here
        if not pHead:
            return pHead
        head = None
        while pHead:
            tmp = pHead.next
            pHead.next = head
            head = pHead
            pHead = tmp
        return head

s = Solution()
s.printListFromTailToHead(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
