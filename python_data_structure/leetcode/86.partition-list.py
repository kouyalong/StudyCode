# coding: utf-8


from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def print_head(self, head):
        ret = head
        ll = list()
        while ret:
            ll.append(ret.val)
            ret = ret.next
        print(ll)

    def partition(self, head: ListNode, x: int) -> ListNode:
        root = ListNode(0, next=head)
        insert_pos = root
        while insert_pos.next and insert_pos.next.val < x:
            insert_pos = insert_pos.next

        p = insert_pos
        while p.next:
            if p.next.val < x:
                tmp = insert_pos.next
                insert_pos.next = p.next
                p.next = p.next.next
                insert_pos.next.next = tmp
                insert_pos = insert_pos.next
            else:
                p = p.next

        return root.next


h = ListNode(1, next=ListNode(4, next=ListNode(3, next=ListNode(2, next=ListNode(5, next=ListNode(2, next=ListNode(1)))))))
h = ListNode(2, next=ListNode(1))
s = Solution()
ret = s.partition(h, 2)
s.print_head(ret)

