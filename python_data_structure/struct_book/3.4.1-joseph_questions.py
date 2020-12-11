# coding: utf-8


from copy import deepcopy


class Node:

	def __init__(self, val, nex=None):
		self.val = val
		self.next = nex


head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
r = head
while r:
	if r.next:
		r = r.next
	else:
		r.next = head
		break


def joseph_questions(rear, number):
	count = 1
	pre = rear
	p = rear.next
	while p.next != p:
		if count == number:
			pre.next = p.next
			p = pre.next
			count = 1
		else:
			pre = pre.next
			p = p.next
			count += 1
	return p.val


joseph_questions(r, 3)
