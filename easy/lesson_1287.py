from collections import Counter
class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        cnt = Counter(arr)
        return max(cnt, key=lambda x:cnt[x])


sol = Solution()
print(sol.findSpecialInteger(arr=[1,1]))