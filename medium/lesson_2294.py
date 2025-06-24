class Solution:

    def __init__(self):
        self.num = None
    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()
        cnt, start, step = 0, 0, 1
        while step < len(nums):

            if nums[step] - nums[start] > k:

                cnt += 1
                start = step
            step += 1
        else:
            if nums[step - 1] - nums[start] <= k:
                cnt += 1
        return cnt
        # for num in nums:
        #     self.num = num
        #     if num - start > k:
        #         cnt += 1
        #         start = num
        # else:
        #     if self.num - start <= k:
        #         cnt += 1
        #
        # return cnt

sol = Solution()
print(sol.partitionArray([3,6,1,2,5], 2))
print(sol.partitionArray([1,2,3], 1))