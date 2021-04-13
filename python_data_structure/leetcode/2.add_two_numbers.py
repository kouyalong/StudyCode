# coding: utf-8


class Node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def add_two_numbers(list1, list2):
    def add_list_number(val1, val2, add_in):
        sum_number = val1 + val2 + add_in
        return int(sum_number % 10), int(sum_number / 10)

    add_flag = 0
    p = q = list1

    while list1 or list2:

        if list1 and list2:
            list1.val, add_flag = add_list_number(list1.val, list2.val, add_flag)
            list2 = list2.next
            if not list1.next:
                list1.next = list2
                list2 = None
            list1 = list1.next
        elif list1 and not list2:
            list1.val, add_flag = add_list_number(list1.val, 0, add_flag)
            list1 = list1.next
        if q.next:
            q = q.next
    if add_flag:
        q.next = Node(1)

    number, index = 0, 0
    while p:
        number += (10 ** index) * p.val
        p = p.next
        index += 1

    return number


l1 = Node(5)
l2 = Node(5)
ret = add_two_numbers(l1, l2)
# print(ret)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)
        more_num = 0
        while l1 or l2 or more_num:
            if l1 and l2:
                sum_num = l1.val + l2.val + more_num
                l1 = l1.next
                l2 = l2.next
            elif l1 and not l2:
                sum_num = l1.val + more_num
                l1 = l1.next
            elif l2 and not l1:
                sum_num = l2.val + more_num
                l2 = l2.next
            else:
                sum_num = more_num
            head.next = ListNode(sum_num % 10)
            more_num = sum_num // 10
            head = head.next
        return root.next


l1 = ListNode(5, next=ListNode(5))
l2 = ListNode(5, next=ListNode(5, next=ListNode(1)))
s = Solution()
ret = s.addTwoNumbers(l1, l2)
while ret:
    print(ret.val)
    ret = ret.next
