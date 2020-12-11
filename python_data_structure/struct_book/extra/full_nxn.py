# coding: utf-8


def full_nxn_matrix(number, begin, size, data):
	"""
	循环 填充nXn的矩阵
	"""
	if size == 0:
		return data, number
	if size == 1:
		data[begin][begin] = number
		return data, number
	i = j = begin
	for _ in range(size - 1):
		data[i][j] = number
		number += 1
		i += 1
	for _ in range(size - 1):
		data[i][j] = number
		number += 1
		j += 1
	for _ in range(size - 1):
		data[i][j] = number
		number += 1
		i -= 1
	for _ in range(size - 1):
		data[i][j] = number
		number += 1
		j -= 1
	return data, number


def full_solution(size):
	if size == 0:
		return [[]]
	if size == 1:
		return [[1]]
	d = [[0 for _ in range(size)] for _ in range(size)]
	start_number = 1
	start_loc = 0
	for lot_size in range(size, 0, -2):
		d, start_number = full_nxn_matrix(start_number, start_loc, lot_size, d)
		start_loc += 1
	return d


ret = full_solution(2)
print(ret)
