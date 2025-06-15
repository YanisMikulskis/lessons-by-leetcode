# class Solution:
#     def maxAdjacentDistance(self, nums: list[int]) -> int:
#         ans = float('-inf')
#         for i in range(len(nums) - 1):
#             if abs(nums[i] - nums[i + 1]) > ans:
#                 ans = abs(nums[i] - nums[i + 1])
#         else:
#             if abs(nums[-1] - nums[0]) > ans:
#                 ans = abs(nums[-1] - nums[0])
#         return ans
#
#
# sol = Solution()
# sol.maxAdjacentDistance([1,2,4])
# sol.maxAdjacentDistance(nums = [7, -4, 3, 1])





class Solution:
    def minimizeMax(self, nums: list[int], p: int) -> int:


        def merge_sort(arr):
            if len(arr) == 1:
                return arr
            middle = len(arr) // 2
            left, right = merge_sort(arr[:middle]), merge_sort(arr[middle:])
            return merge(left, right)


        def merge(left, right):
            res = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            res.extend(left[i:]), res.extend(right[j:])
            return res


        nums = merge_sort(nums)


        results = [abs(nums[i] - nums[i + 1]) for i in range(0, len(nums) - 1, 2)]

        return max(results[:p])





sol = Solution()
# sol.minimizeMax(nums = [10,1,2,7,1,3], p = 2)
# sol.minimizeMax(nums = [1, 2, 3, 100, 101, 102], p = 2)
sol.minimizeMax([4,0,2,1,2,5,5,3], p=3)