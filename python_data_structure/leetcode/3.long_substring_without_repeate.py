# coding: utf-8


def long_string_without_repeating(string):
	length = 0
	start = 0
	string_hash = dict()
	for i, val in enumerate(string):
		start = max(start, string_hash.get(val, -1) + 1)
		length = max(length, i - start + 1)
		string_hash[val] = i
	return length


s = "xyzxlkjh"
ret = long_string_without_repeating(s)
print(ret)
