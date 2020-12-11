# coding: utf-8


class Node:
	def __init__(self, coe, exp, nex=None):
		self.coe = coe
		self.exp = exp
		self.nex = nex


def merge_node(head1, head2):

	p = head1 if head1.exp < head2.exp else head2
	while head1 and head2:
		if head1.exp > head2.exp:
			tmp = head2
			head2 = head2.nex
			tmp.nex = head1
			head1 = tmp
		elif head1.exp < head2.exp:
			if head1.nex:
				if head1.nex.exp > head2.exp:
					tmp = head2
					head2 = head2.nex
					tmp.nex = head1.nex
					head1.nex = tmp
			else:
				head1.nex = head2
				head2 = head2.nex
		else:
			head1.coe += head2.coe
			head2 = head2.nex

		if head1.nex:
			head1 = head1.nex
	return p


a_head = Node(7, 0, Node(12, 3, Node(-2, 8, Node(5, 12, Node(1, 19)))))
b_head = Node(4, 1, Node(6, 3, Node(2, 8, Node(5, 20, Node(7, 28)))))

ret = merge_node(a_head, b_head)
while ret:
	print(ret.coe, ret.exp)
	ret = ret.nex
