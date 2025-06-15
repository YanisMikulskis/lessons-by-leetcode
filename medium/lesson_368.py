import random


class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        if len(nums) == 1:
            return nums
        idx_cur = 0
        step = idx_cur + 1

        cur = nums[idx_cur]
        currents = [cur]

        all_currents = []

        while step < len(nums):

            if cur % nums[step] == 0 or nums[step] % cur == 0:
                currents.append(nums[step])
                cur = currents[-1]

            step += 1

            if step == len(nums):
                print(nums)
                # nums = nums[1:] if len(currents) <= 1 else [i for i in nums if i not in currents]
                if not all_currents:
                    all_currents.append(currents)
                else:
                    if len(currents) >= len(all_currents[-1]):
                        all_currents.append(currents)

                if len(nums) < len(currents):
                    return max(all_currents, key=lambda x:len(x))

                idx_cur += 1
                step = idx_cur + 1
                cur = nums[idx_cur]
                currents = [cur]
                # cur, step = nums[0], 1

                # currents = [nums[i]]
                # cur, step = nums[0], 1

        print(all_currents)
        return max(all_currents, key=lambda x:len(x))



                # cur = currents[-1]











sol = Solution()
# print(sol.largestDivisibleSubset(nums = [3, 6, 9, 12, 18]))
# print(sol.largestDivisibleSubset([1, 2, 4, 8]))
# print(sol.largestDivisibleSubset([1,2,3]))
# print(sol.largestDivisibleSubset([5, 10, 15, 20]))
# print(sol.largestDivisibleSubset([2, 3, 4, 6, 8, 12, 24]))
# print(sol.largestDivisibleSubset([7, 11, 13, 17]))
# print(sol.largestDivisibleSubset([7, 11, 13, 17, 20, 40]))
# print(sol.largestDivisibleSubset([1, 3, 9, 27, 81]))
# print(sol.largestDivisibleSubset([2, 5, 10, 20, 25, 50]))
# print(sol.largestDivisibleSubset([1, 2, 3, 4, 6, 12]
#
# ))
# print(sol.largestDivisibleSubset([2, 3, 4, 6, 8, 12, 24]))
# print(sol.largestDivisibleSubset([2,4,6,9,19,81,729]))
def canPartition(nums):
    total_sum = sum(nums)
    print(f'total sum = {total_sum}')
    if total_sum % 2 != 0:
        return False

    target = total_sum // 2
    print(f'target = {target}')
    dp = [False] * (target + 1)
    print(f'dp = {dp}')
    dp[0] = True  # База: сумма 0 достижима
    print(dp)
    for num in nums:
        print(f'num = {num}')
        for j in range(target, num - 1, -1):
            print(f'j = {j}')
            if dp[j - num]:
                dp[j] = True
                print(f'промеж dp = {dp}')
            print(f'----')
        if dp[target]:  # Ранний выход
            return True
    return dp[target]


canPartition(nums = [1, 5, 11, 5])



#2 4 8 24
#2 4 12 24
#
