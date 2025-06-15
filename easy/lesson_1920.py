class Solution:
    '''
    Вам дан массив nums, представляющий собой перестановку чисел от 0 до n-1 (где n = len(nums)).
    Это значит, что в массиве nums содержатся все числа от 0 до n-1 без повторений.

    Постройте новый массив ans, такой что:

    ans[i] = nums[nums[i]]
    для каждого индекса i от 0 до n - 1.

    Верните массив ans.

    🔹 Пример 1:
    Вход: nums = [0, 2, 1, 5, 3, 4]
    ans[0] = nums[nums[0]] = nums[0] = 0
    ans[1] = nums[nums[1]] = nums[2] = 1
    ans[2] = nums[nums[2]] = nums[1] = 2
    ans[3] = nums[nums[3]] = nums[5] = 4
    ans[4] = nums[nums[4]] = nums[3] = 5
    ans[5] = nums[nums[5]] = nums[4] = 3
    Выход: [0, 1, 2, 4, 5, 3]
    '''
    def buildArray(self, nums: list[int]) -> list[int]:
        return [nums[num] for num in nums]

sol = Solution()
sol.buildArray(nums = [0, 2, 1, 5, 3, 4])
sol.buildArray(nums = [5, 0, 1, 2, 3, 4])
sol.buildArray(nums = [5,0,1,2,3,4])