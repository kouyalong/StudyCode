# coding: utf-8


def convert(s: str, numRows: int) -> str:
	if numRows == 1:
		return s
	cs = ""
	index_set = set()
	for i in range(numRows):
		count = 0
		left = (2 * numRows - 2) * count + i
		while 0 <= left < len(s):
			right = left + (2 * (numRows - i) - 2)
			if left not in index_set:
				cs += s[left]
				index_set.add(left)
			if 0 <= right < len(s) and right not in index_set:
				cs += s[right]
				index_set.add(right)
			count += 1
			left = (2 * numRows - 2) * count + i
	return cs


def cc(s, numRows):
	if len(s) < numRows or numRows == 1:
		return s
	dp = [''] * numRows
	index = 0
	step = 1
	for i in s:
		dp[index] += i
		index += step
		if index == numRows - 1:
			step = -1
		if index == 0:
			step = 1
	return ''.join(dp)


ss = "LEE"
"""
LEETCODEISHIRING
LCIRETOESIIGEDHN
LCIRETOESIIGEDHN
0   4   8     12
1 3 5 7 9  11 13
2   6   10    14
"""

num_rows = 3
ret = convert(ss, num_rows)
print(ret)
