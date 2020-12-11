# coding: utf-8


def max_common_factor(m, n):
	"""m, n的最大公约数"""
	r = m % n
	while r != 0:
		m = n
		n = r
		r = m % n
	return n


def egypt_function(a, b):
	pass


pr = max_common_factor(56, 24)
print(pr)


def fibonacci(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(9))
