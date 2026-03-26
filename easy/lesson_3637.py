class Solution:
    def isTrionic(self, nums):
        ans = [None] * 3
        idx: int = 0
        for i in range(len(nums) - 1):

            if nums[i] < nums[i + 1]:
                if idx == 1:
                    idx = 2
                    ans[idx] = 1
                else:
                    ans[idx] = 1
            elif nums[i] == nums[i + 1]:
                return False
            else:
                if ans == [1,0,1]:
                    return False
                idx = 1
                ans[idx] = 0
        return True if ans == [1,0,1] else False

sol = Solution()
# print(sol.isTrionic(nums = [1,3,5,4,2,6]))



arr = list(range(5))

subs = []

l,r = 0,1
while l < len(arr) - 1:
    if r == len(arr) + 1:
        l += 1
        r = l + 1
    subs.append(arr[l:r])
    r += 1

print(subs)

for i in (1, 2);
    pr