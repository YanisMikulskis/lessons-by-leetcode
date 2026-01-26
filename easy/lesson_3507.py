class Solution:
    def minimumPairRemoval(self, nums):
        res = 0
        def check_lst(lst):
            for i in range(len(lst) - 1):
                if lst[i] > lst[i + 1]:
                    return False
            return True

        while not check_lst(nums):
            min_el = None
            idx1, idx2 = None, None
            for i in range(len(nums) - 1):
                el = nums[i] + nums[i + 1]
                if min_el is None:
                    min_el = el
                else:
                    if el < min_el:
                        min_el, idx1, idx2 = el, i, i + 1
            else:
                nums[idx1:idx2 + 1] = [min_el]
                res += 1

        return res

sol = Solution()
print(sol.minimumPairRemoval([5,2,3,1]))
print(sol.minimumPairRemoval([1,2,3,4,5]))
arr = [1,2,3,4,5]
print(arr)
arr[1:3] = [5]
print(arr)