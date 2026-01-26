class Solution:
    def sortArrayByParityII(self, nums: list[int]):
        #
        # res = []
        # i = 0
        # while i < len(nums):
        #     if nums[i] % 2 == 0:
        #         res += [nums[i], None]
        #         nums.pop(i)
        #         i -= 1
        #     i += 1
        #
        # for i in range(len(res)):
        #     if res[i] is None:
        #         res[i] = nums.pop(0)
        j = 1
        print(nums)



        for i in range(0, len(nums), 2):
            if nums[i] % 2 != 0:
                while nums[j] % 2 != 0:
                    j += 1
                nums[i], nums[j] = nums[j], nums[i]

        return nums

sol = Solution()
print(sol.sortArrayByParityII(nums = list(range(1,7))))


