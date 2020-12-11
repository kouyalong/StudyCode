# coding: utf-8


def data_tower(tower_dict):
	length = len(tower_dict)
	if length == 0:
		return 0
	if length == 1:
		return tower_dict[0][0]

	dp = [[0 for _ in range(length)] for _ in range(length)]
	for i in range(length):
		dp[length-1][i] = tower_dict[length-1][i]

	for i in range(length-2, -1, -1):
		for j in range(i+1):
			dp[i][j] = tower_dict[i][j] + max(dp[i+1][j], dp[i+1][j+1])
	return dp[0][0]


td = [[8, 0, 0, 0, 0], [12, 15, 0, 0, 0], [3, 9, 6, 0, 0], [8, 10, 5, 12, 0], [16, 4, 18, 10, 9]]
td = [[1]]
ret = data_tower(td)
print(ret)
