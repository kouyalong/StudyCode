class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_list, d_list = list(), list()
        length = len(senate)
        for i in range(length):
            if senate[i] == "R":
                r_list.append(i)
            else:
                d_list.append(i)
        while r_list and d_list:
            r_first = r_list.pop(0)
            d_first = d_list.pop(0)
            if r_first < d_first:
                r_list.append(r_first+length)
            else:
                d_list.append(d_first+length)
        if r_list:
            return "Radiant"
        else:
            return "Dire"


s = Solution()
print(s.predictPartyVictory("RDD"))
