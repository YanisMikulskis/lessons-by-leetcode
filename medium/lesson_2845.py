from collections import Counter
class Solution:
    def countInterestingSubarrays(self, nums: list[int], modulo: int, k: int) -> int:
        def func(lst):
            for i in range(len(lst)):
                for j in range(i, len(lst)):
                    yield lst[i:j + 1]

        def check(l):
            return True if len([i for i in l if i % modulo == k]) % modulo == k else False

        res = 0
        for sub in func(nums):
            if check(sub):
                res += 1
        return res


sol.countInterestingSubarrays(nums = [3,1,9,6], modulo = 3, k = 0)