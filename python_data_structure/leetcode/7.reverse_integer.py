# coding: utf-8


def reverse_integer(x: int) -> int:
	if x < 0:
		return -reverse_integer(-x)
	res = 0
	while x:
		res = res * 10 + x % 10
		x //= 10
	return res if res <= 0x7fffffff else 0


ret = reverse_integer(12000)
print(ret)
