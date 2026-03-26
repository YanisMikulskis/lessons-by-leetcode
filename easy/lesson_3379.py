class Solution:
    def constructTransformedArray(self, nums: list) -> list:
        ans, idx = [], 0
        while idx < len(nums):
            step = idx + nums[idx]
            print(f'step = {step % 1}')
            if abs(step) >= len(nums):
                step %= len(nums)

            print(f'step = {step}')
            ans.append(nums[step])
            idx += 1
        return ans

sol = Solution()
# sol.constructTransformedArray([1, 2, 3, 4, 5])
sol.constructTransformedArray([-10, 9])
