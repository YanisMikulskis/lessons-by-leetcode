class Solution:
    def minPairSum(self, nums):
        nums.sort()

        max_sum = None

        for i in range(len(nums)//2):
            ans = nums[i] + nums[len(nums) - 1 - i]
            if max_sum is None:
                max_sum = ans
            else:
                if ans > max_sum:
                    max_sum = ans

        return max_sum

sol = Solution()
print(sol.minPairSum(nums = [3,5,2,3]))