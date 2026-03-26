from collections import Counter


class Solution:
    def containsDuplicate(self, nums):

        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False

        
        return True if max(Counter(nums).values()) > 1 else False

sol = Solution()
sol.containsDuplicate([1,2,3,1])