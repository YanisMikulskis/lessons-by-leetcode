class Solution:
    '''
    Дан целочисленный массив nums и неотрицательное целое число k.

    За одну операцию можно увеличить или уменьшить любой элемент массива на 1.

    Найди минимальное количество операций, чтобы медиана массива стала равной k.

    ℹ️ Примечание:
    Медиана массива определяется как средний элемент отсортированного массива.
    Если длина массива чётная, выбирается бОльший из двух средних значений.

    🧪 Примеры:
    ✅ Пример 1:

    Вход: nums = [2, 5, 6, 8, 5], k = 5
    Выход: 0
    Объяснение: массив уже имеет медиану 5 (отсортированный: [2, 5, 5, 6, 8])


    Input: nums = [2,5,6,8,5], k = 7

    Output: 3

    Explanation:

    We can add one to nums[1] twice and add one to nums[2] once to obtain [2, 7, 7, 8, 5].
    '''
    def minOperationsToMakeMedianK(self, nums: list[int], k: int) -> int:

    #     nums = self.sort_met(nums)
    #     med, ans = nums[len(nums) // 2], 0
    #     while med != k:
    #         nums[len(nums) // 2] = nums[len(nums) // 2] + 1 if med < k else  nums[len(nums) // 2] - 1
    #         ans += 1
    #         nums = self.sort_met(nums)
    #         med = nums[len(nums) // 2]
    #     return ans
    #
    # def sort_met(self, lst):
    #
    #     def merge_sort(arr):
    #         if len(arr) <= 1:
    #             return arr
    #         middle = len(arr) // 2
    #         left, right = merge_sort(arr[:middle]), merge_sort(arr[middle:])
    #         return merge(left, right)
    #
    #     def merge(left, right):
    #         result = []
    #         i = j = 0
    #         while i < len(left) and j < len(right):
    #             if left[i] < right[j]:
    #                 result.append(left[i])
    #                 i += 1
    #             else:
    #                 result.append(right[j])
    #                 j += 1
    #         result.extend(left[i:]), result.extend(right[j:])
    #         return result
    #
    #     return merge_sort(lst)
        nums.sort()
        ans = 0
        n = len(nums)
        med = n // 2
        for i in range(med + 1):
            if nums[i] < k:
                ans += k - nums[i]

        for i in range(med + 1, n):
            if nums[i] > k:
                ans += nums[i] - k
        print(f'ans = {ans}')









        # arr = [1,2,3,4,5,6,7,8,9, 10]
        # n = 7
        #
        # left = 0
        # right = len(arr) - 1
        # mid = right // 2
        #
        # while n != mid:
        #     mid = (right + left) // 2
        #     if arr[mid] == n:
        #         return mid
        #     if n < arr[mid]:
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        # print(f'mid = {mid}')



sol = Solution()
print(sol.minOperationsToMakeMedianK(nums = [2, 5, 6, 8, 5], k = 4))
print(sol.minOperationsToMakeMedianK(nums = [2,5,6,8,5], k = 7))
print(sol.minOperationsToMakeMedianK(nums = [1,2,3,4,5,6], k = 4))
