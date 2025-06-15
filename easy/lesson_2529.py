class Solution:
    def maximumCount(self, nums: list[int]) -> int: #оптимизированный способ

        left = 0
        right = len(nums) - 1

        if nums[left] > 0 or nums[right] < 0:
            return len(nums)


        while left < right:
            middle = (left + right) // 2
            if nums[middle] < 0:
                left = middle + 1
            else:
                right = middle

        if right < 0:
            return 0

        if nums[right] == 0:
            while nums[right] == 0:
                right += 1
                if right > len(nums) - 1:
                    break



        return max([len(nums[:left]), len(nums[right:])])

    def met(self, nums): # неоптимизированный способ
        negative, positive = 0,0
        for i in nums:
            if i > 0:
                positive += 1
            else:
                if i == 0:
                    continue
                else:
                    negative -= 1
        return max([negative, positive])






sol = Solution()
print(sol.maximumCount(nums = [-2,-1, 2, 4, 5,6, 7]))
print()
print(sol.maximumCount(nums = [-3,-2,-1,0,0,1,2]))
print()
print(sol.met(nums = [0, 0 ,0]))
print(sol.maximumCount([5,20,66,1314]))
print(sol.maximumCount([-1563,-236,-114,-55,427,447,687,752,1021,1636]))


print(sol.met(nums = [-2,-1, 2, 4, 5,6, 7]))
# print()
print(sol.met(nums = [-3,-2,-1,0,0,1,2]))
print()
print(sol.met(nums = [0, 0 ,0]))
print(sol.met([5,20,66,1314]))
print(sol.met([-1563,-236,-114,-55,427,447,687,752,1021,1636]))