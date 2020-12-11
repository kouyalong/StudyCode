# coding: utf-8


class Node:

	def __init__(self, val, next=None):
		self.val = val
		self.next = next


def add_two_numbers(list1, list2):

	def add_list_number(val1, val2, add_in):
		sum_number = val1 + val2 + add_in
		return int(sum_number % 10), int(sum_number/10)

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
print(ret)
