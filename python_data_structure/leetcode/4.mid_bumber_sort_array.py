# coding: utf-8


def find_mid_number(array1, array2):
	n = len(array1) + len(array2)
	if n % 2 == 1:
		return findkth(array1, array2, n//2 + 1)
	else:
		smaller = findkth(array1, array2, n//2)
		bigger = findkth(array1, array2, n//2 + 1)
		return (smaller + bigger) / 2.0


def findkth(a, b, k):
	if len(a) == 0:
		return b[k-1]
	if len(b) == 0:
		return a[k-1]

	if k == 1:
		return min(a[0], b[0])

	ap = a[k//2-1] if len(a) >= k/2 else None
	bp = b[k//2-1] if len(b) >= k/2 else None

	if bp is None or (ap is not None and ap < bp):
		return findkth(a[k//2:], b, k-k//2)
	else:
		return findkth(a, b[k//2:], k-k//2)


ret = find_mid_number([1, 3], [3, 3, 3])
print(ret)
