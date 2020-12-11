# coding: utf-8


class Solution:
	def longestPalindrome(self, s: str) -> str:
		size = len(s)
		if size < 2:
			return s

		dp = [[False for _ in range(size)] for _ in range(size)]

		max_len = 1
		start = 0

		for i in range(size):
			dp[i][i] = True

		for j in range(1, size):
			for i in range(j - 1, -1, -1):
				if s[i] == s[j]:
					if j - i < 3:
						dp[i][j] = True
					else:
						dp[i][j] = dp[i + 1][j - 1]
				else:
					dp[i][j] = False

				if dp[i][j]:
					cur_len = j - i + 1
					if cur_len > max_len:
						max_len = cur_len
						start = i
		return s[start:start + max_len]

	def longestPalindrome2(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		n = len(s)
		maxl = 0
		start = 0
		for i in range(n):
			print(i, maxl)
			if i - maxl >= 1 and s[i-maxl-1: i+1] == s[i-maxl-1: i+1][::-1]:
				start = i - maxl - 1
				maxl += 2
				continue
			if i - maxl >= 0 and s[i-maxl: i+1] == s[i-maxl: i+1][::-1]:
				start = i - maxl
				maxl += 1
		return s[start: start + maxl]


sl = Solution()
string = "aaaaaaaa123321aaa"
ret = sl.longestPalindrome2(string)
print(ret)
