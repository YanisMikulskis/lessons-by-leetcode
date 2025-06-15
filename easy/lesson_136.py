from collections import Counter
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for i in nums:
            result ^= i
        return result



sol = Solution()
print(sol.singleNumber(nums = [4,1,2,1,2]))