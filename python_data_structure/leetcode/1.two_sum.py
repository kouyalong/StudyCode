# coding: utf-8


def two_sum(array, target):
	value2index = dict()

	for i in range(len(array)):
		diff = target - array[i]
		if value2index.get(diff) is not None:
			return [value2index[diff], i]
		value2index[array[i]] = i
	return []


ret = two_sum([2, 7, 11, 15], 9)
print ret
