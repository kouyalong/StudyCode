# coding: utf-8


class Node:

	def __init__(self, val, nxt=None):
		self.val = val
		self.next = nxt


def reserve_linked(head):
	p = None
	while head:
		tmp = head
		head = head.next
		tmp.next = p
		p = tmp
	return p


def jungle_linked_circle(head):
	if not head:
		return False
	fast = head
	slow = head
	while fast and slow:
		if fast.next and fast.next.next:
			fast = fast.next.next
		else:
			fast = None
		if slow.next:
			slow = slow.next
		else:
			slow = None
		if fast and slow and fast == slow:
			return True
	return False


def merge_two_sorted_linked(l1, l2):
	head = Node(-1)
	first = head
	while l1 and l2:
		if l1.val > l2.val:
			head.next = l2
			l2 = l2.next
		else:
			head.next = l1
			l1 = l1.next
		head = head.next
	if not l1:
		head.next = l2
	elif not l2:
		head.next = l1
	return first.next


def merge_two_sorted_linked2(l1, l2):
	if not l1:
		return l2
	if not l2:
		return l1

	l1, l2 = (l1, l2) if l1.val < l2.val else (l2, l1)
	head = l1
	while l1.next and l2:
		if l1.val <= l2.val <= l1.next.val:
			tmp = l2
			l2 = l2.next
			tmp.next = l1.next
			l1.next = tmp
			l1 = l1.next
		elif l1.next.val < l2.val:
			l1 = l1.next
	if l2:
		l1.next = l2
	return head


def merge_two_sorted_linked3(nums1, m, nums2, n):
	p1 = m - 1
	p2 = n - 1
	p = m + n - 1
	while p1 >= 0 and p2 >= 0:
		if nums1[p1] < nums2[p2]:
			nums1[p] = nums2[p2]
			p2 -= 1
		else:
			nums1[p] = nums1[p1]
			p1 -= 1
		p -= 1
	nums1[:p2+1] = nums2[:p2+1]


def linked_k_number(lp, k):
	count = 0
	head = lp
	while lp:
		if count >= k:
			head = head.next
		lp = lp.next
		count += 1
	if k > count:
		return -1
	return head.val


last_linked = Node(8)
new_linked = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, last_linked))))))
last_linked.next = new_linked

linked1 = Node(0, Node(5, Node(8, Node(11, Node(19, Node(26))))))
linked2 = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(36, Node(45, Node(55, Node(65))))))))))

if __name__ == "__main__":
	# new_linked = Node
	# nl = reserve_linked(new_linked)
	# while nl:
	# 	print(nl.val)
	# 	nl = nl.next

	# ret = jungle_linked_circle(new_linked)
	# print(ret)
	#
	# ret = merge_two_sorted_linked2(linked1, linked2)
	# while ret:
	# 	print(ret.val)
	# 	ret = ret.next

	# n1 = [1, 3, 5, 7, 9]
	# n1m = 5
	# n2 = [2, 4, 6, 8, 10, 12, 14, 16]
	# n2m = 8
	# for i in range(n2m):
	# 	n1.append(-1)
	# merge_two_sorted_linked3(n1, n1m, n2, n2m)
	# print(n1)

	print(linked_k_number(linked2, 4))
