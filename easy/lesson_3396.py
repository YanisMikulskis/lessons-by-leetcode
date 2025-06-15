from collections import Counter
class Solution:
    def minimumOperations(self, nums: list[int]) -> int:



        def func(lst, step):
            if len(lst) == 0 or max(Counter(lst).values()) == 1:
                return step
            return func(lst[3:], step + 1)
        return func(nums, 0)




sol = Solution()
print(sol.minimumOperations([1,2,3,4,2,3,3,5,7]))
print(sol.minimumOperations([6,7,8,9]))
# print(sol.minimumOperations([1,2,3,4,2,3,3,5,7]))
