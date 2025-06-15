from collections import Counter
class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        # result = set()
        # for num in nums:
        #     if num < k:
        #         return -1
        #     elif num > k:
        #         result.add(num)
        # return len(result)

        # step = 0
        # for i in range(k):
        #     nums = [i for i in nums if i != max(nums)]
        #     step += 1
        # return f'step = {step}'

        if len(nums) == len(set(nums)):
            if k > min(nums):
                return -1




        step = 0
        while set(nums) != {k}:
            first_max, second_max = float('-inf'), float('-inf')
            for num in nums:
                if num > first_max:
                    second_max = first_max
                    first_max = num
                elif num > second_max and num != first_max:
                    second_max = num
            print(f'dd')
            nums = list(map(lambda x: second_max if x == first_max else x, nums))
            if len(Counter(nums)) == 1 and nums[0] != k:
                step += 1
                nums = {k}
            step += 1
        return step












        # step = 0
        # arr = [1,2,5,100, 100, 98, 5]
        # first = second = float('-inf')
        # for i in arr:
        #     if i > first:
        #         second = first
        #         first = i
        #     elif i > second and i != first:
        #         second = i











sol = Solution()



print(sol.minOperations(nums = [2], k = 1))
nums = [10,10,4,10]
