# coding: utf-8

# coding: utf-8


class Node:

	def __init__(self, value, next=None):
		self.value = value
		self.next = next


def new_merge_two_sorted_array(array1, array2):
	if not array1 and not array2:
		return None
	elif array1 and array2:
		p1, p2 = (array1, array2) if array1.value < array2.value else (array2, array1)
	elif array1 and not array2:
		p1, p2 = array1, None
	else:
		p1, p2 = array2, None

	p = p1
	while p1.next or p2:
		while p1.next and p1.value == p1.next.value:
			p1.next = p1.next.next

		if p1.next and p2:
			if p1.next.value < p2.value:
				p1 = p1.next
			elif p1.next.value > p2.value:
				tmp = p1.next
				p1.next = p2
				p2 = p2.next
				p1.next.next = tmp
			else:
				p2 = p2.next
				p1 = p1.next

		elif p1.next and not p2:
			p1 = p1.next

		elif not p1.next and p2:
			if p1.value == p2.value:
				p2 = p2.next
			else:
				p1.next = p2
				p2 = p2.next
				p1 = p1.next

	return p


def merge_two_sorted_array(array1, array2):

	p1, p2 = (array1, array2) if array1.value < array2.value else (array2, array1)

	p = p1
	while p1.next and p2:
		while p1.next and p1.value == p1.next.value:
			p1.next = p1.next.next

		if p1.next.value == p2.value:
			p2 = p2.next
		elif p1.next.value > p2.value:
			tmp = p1.next
			p1.next = p2
			p2 = p2.next
			p1.next.next = tmp

		else:
			p1 = p1.next
	while p2:
		if p1.value == p2.value:
			p2 = p2.next
		else:
			p1.next = p2
			p2 = p2.next
			p1 = p1.next

	return p


def max_long_string_not_rep(string):
	start, end, tmp_s = 0, 0, 0
	char_dict = dict()
	for i in range(len(string)):
		tmp_s = max(tmp_s, char_dict.get(string[i], -1) + 1)
		start, end = (start, end) if (end - start) >= (i - tmp_s) else (tmp_s, i)
		char_dict[string[i]] = i
	return string[start:end+1]


b = Node(1, Node(1, Node(2, Node(4, Node(6, Node(7, Node(8)))))))
a = Node(1, Node(1, Node(2, Node(4, Node(6, Node(7, Node(8)))))))

ret = new_merge_two_sorted_array(a, b)
while ret:
	print(ret.value)
	ret = ret.next


test_string = "xyzxlkjh"
ret_str = max_long_string_not_rep(test_string)
print(ret_str)
