class Solution:
    def minimumCost(self, nums):
        # res = []
        #
        #
        # left, right = 1,2
        # ans = float('inf')
        # while left < len(nums) - 1:
        #     res.append([nums[:left], nums[left:right], nums[right:]])
        #
        #
        #     if nums[:left][0] +
        #     if right < len(nums) - 1:
        #         right += 1
        #     else:
        #         left += 1
        min1, min2 = float('inf'), float('inf')
        ans = nums[0]
        for num in nums[1:]:
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num
        ans += min1 + min2
        return ans




sol = Solution()
print(sol.minimumCost(nums = [1,2,3,12]))