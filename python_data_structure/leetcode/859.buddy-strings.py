

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        length_a, length_b = len(A), len(B)
        if length_a != length_b:
            return False

        fot_item = []
        item2count = {}
        for i in range(length_a):
            item2count.setdefault(A[i], 0)
            item2count[A[i]] += 1
            if A[i] != B[i]:
                fot_item.append(i)
        if len(fot_item) == 2:
            if A[fot_item[0]] == B[fot_item[1]] and A[fot_item[1]] == B[fot_item[0]]:
                return True
        if not fot_item:
            flag = False
            for _, c in item2count.items():
                if c > 1:
                    flag = True
                    break
            if flag:
                return True
            else:
                return False
        return False


s = Solution()
print(s.buddyStrings("ab", "ab"))
