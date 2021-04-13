# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        pk = root = ListNode(-1)
        pk.next = head
        for _ in range(left-1):
            pk = pk.next

        cur = pk.next
        for _ in range(right-left):
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = pk.next
            pk.next = tmp
        return root.next


"""
1 2 3 4 5 6
1 3 2 4 5 6  1
1 4 3 2 5 6  2 
1 4 3 2 5 6
"""
hl = ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4, next=ListNode(5, next=ListNode(6))))))
# hl = ListNode(1, next=ListNode(2))

s = Solution()
rn = s.reverseBetween(hl, 2, 4)
while rn:
    print(rn.val)
    rn = rn.next
