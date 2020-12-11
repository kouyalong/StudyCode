# coding: utf-8


def binary_found(array, low, high, number):

	if low == high:
		if array[low] == number:
			return low
		else:
			return -1

	mid = (low + high) // 2
	if array[mid] < number:
		return binary_found(array, mid+1, high, number)
	elif array[mid] > number:
		return binary_found(array, low, mid-1, number)
	else:
		return mid


def binary_search(array, number):
	return binary_found(array, 0, len(array)-1, number)


a = [6, 7, 8, 9, 10]
n = 6
ret = binary_search(a, n)
print(ret)
