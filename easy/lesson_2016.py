import itertools


class Solution:
    '''
    Вам дан массив целых чисел nums размером n (индексация с 0).
    Найдите максимальную разность nums[j] - nums[i] таких элементов, для которых:

    0 <= i < j < n
    nums[i] < nums[j]
    Если таких пар (i, j) не существует, верните -1.

    Примеры:
    Пример 1:

    Вход: nums = [7, 1, 5, 4]
    Выход: 4
    Пояснение:
    nums[1] = 1 и nums[2] = 5 → 5 - 1 = 4
    - Это максимальная разность при выполнении условия nums[i] < nums[j]
    '''
    def maximumDifference(self, nums: list[int]) -> int:

        result = float('-inf')
        i, j = 0, len(nums) - 1
        while j > 0:
            if i == j:
                i,j = 0, j -1
            if (nums[j] - nums[i]) > result:
                result = nums[j] - nums[i]
            i += 1
        if result <= 0:
            return -1
        return result

# sol = Solution()
# print(sol.maximumDifference([7,1,5,4]))
# print()
# print(sol.maximumDifference([9, 4, 3, 2]))
# # print()
# print(sol.maximumDifference([1, 5, 2, 10]))
# # print()
# print(sol.maximumDifference([2, 3, 10, 6, 4, 8, 1]))


# # ____________________
# from itertools import permutations
# n = 3
# arr = [1,2,2]
# print(list(permutations(arr)))


nums = [3,6,1,2,5]
k = 2
def func_sort(arr):
    def merge(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge(arr[:mid])
        right = merge(arr[mid:])
        return merge_sort(left, right)
    def merge_sort(left,right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    return merge(arr)


nums = func_sort(nums)
print(nums)


res = []
cnt = 0
start = 0
# for num in range(len(nums)):
#     if nums[num] - nums[start] > k:
#         res.append(nums[start:num])
#         start = num
#         cnt += 1
#
# print(res)
# print(cnt)
count = 0
for num in nums:
    print(f'Текущий: {num}, старт: {start}, разница: {num - start}')
    if num - start > k:
        count += 1
        start = num
        print(f'Новая группа начинается с {start}')
print(count)



