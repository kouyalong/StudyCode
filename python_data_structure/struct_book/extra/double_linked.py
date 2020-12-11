# coding: utf-8


class Node:

	def __init__(self, val, prev=None, nex=None):
		self.val = val
		self.prev = prev
		self.next = nex


def reserve(head):
	curt = None
	while head:
		curt = head
		head = curt.next
		curt.next = curt.prev
		curt.prev = head
	return curt


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n1.next = n2

n2.prev = n1
n2.next = n3

n3.prev = n2
n3.next = n4

n4.prev = n3
n4.next = n5

n5.prev = n4


ret = reserve(n1)

while ret:
	print(ret.val)
	ret = ret.next
