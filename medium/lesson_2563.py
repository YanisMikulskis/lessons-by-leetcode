class Solution:
    '''
    Условие задачи

    Дан массив целых чисел nums с индексацией с 0, размером n, и два целых
    числа lower и upper. Необходимо вернуть количество "честных" пар.

    Пара (i, j) называется "честной", если:

    0 <= i < j < n, и
    lower <= nums[i] + nums[j] <= upper
    Пример 1

    Входные данные:

    nums = [0,1,7,4,4,5], lower = 3, upper = 6
    Выходные данные:

    6
    Объяснение:
    Существует 6 честных пар:

    (0,1) → nums[0] + nums[1] = 0 + 1 = 1 (не подходит)
    (0,2) → 0 + 7 = 7 (не подходит)
    (0,3) → 0 + 4 = 4 (подходит)
    (0,4) → 0 + 4 = 4 (подходит)
    (0,5) → 0 + 5 = 5 (подходит)
    (1,2) → 1 + 7 = 8 (не подходит)
    (1,3) → 1 + 4 = 5 (подходит)
    (1,4) → 1 + 4 = 5 (подходит)
    (1,5) → 1 + 5 = 6 (подходит)
    (2,3) → 7 + 4 = 11 (не подходит)
    (2,4) → 7 + 4 = 11 (не подходит)
    (2,5) → 7 + 5 = 12 (не подходит)
    (3,4) → 4 + 4 = 8 (не подходит)
    (3,5) → 4 + 5 = 9 (не подходит)
    (4,5) → 4 + 5 = 9 (не подходит)
    Подходящие пары: (0,3), (0,4), (0,5), (1,3), (1,4), (1,5) - всего 6.
    '''
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        nums.sort()
        print(nums)
        i,j = 0,1
        res = 0
        while i < len(nums) - 1:
            if lower <= nums[i] + nums[j] <= upper:
                res += 1
            j += 1
            if j == len(nums):
                i += 1
                j = i + 1
        return res

        # lower, upper, result = abs(lower), abs(upper), 0
        # nums = [abs(i) for i in nums]
        # print(nums)
        # nums = [i for i in nums if i <= upper]
        #
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if lower <= nums[i] + nums[j] <= upper:
        #             result += 1
        # return result


sol = Solution()
print(sol.countFairPairs(nums = [0,1,7,4,4,5], lower = 3, upper = 6))
print(sol.countFairPairs(nums = [1,7,9,2,5], lower = 11, upper = 11))
print(sol.countFairPairs([-5,-7,-5,-7,-5], -12, -12))
print(sol.countFairPairs([-1,0], -1, 0))
print(sol.countFairPairs([0,0,0,0,0,0],0, 0))


# def countFairPairs(nums, lower, upper):
    # nums.sort()  # Сортируем массив
    # count = 0
    # n = len(nums)
    # print(f'sort num = {nums}')
    #
    # for i in range(n):
    #     left = lower - nums[i]
    #     print(f'left = {left}')
    #     right = upper - nums[i]
    #     print(f'right = {right}')
    #
    #
    #     # Находим первый j > i, где nums[j] >= left (левую границу)
    #     low = i + 1
    #     print(f'low = {low}')
    #     high = n - 1
    #     print(f'hight = {high}')
    #     print()
    #     first_valid = n  # Если не найдётся, то j = n (не учитываем)
    #     print(f'first_valid = {first_valid}')
    #
    #     while low <= high:
    #         mid = (low + high) // 2
    #         print(f'mid = {mid}  nums[mid] = {nums[mid]}')
    #         if nums[mid] >= left:
    #             first_valid = mid
    #             high = mid - 1
    #         else:
    #             low = mid + 1
    #             print(f'low = {low}')
    #     # Находим последний j > i, где nums[j] <= right (правую границу)
    #     low = i + 1
    #     print(f'low = {low}')
    #     high = n - 1
    #     print(f'hight = {high}')
    #     last_valid = i  # Если не найдётся, то j = i (не учитываем)
    #     print(f'last_valid = {last_valid}')
    #
    #     while low <= high:
    #         mid = (low + high) // 2
    #         print(f'mid = {mid}  nums[mid] = {nums[mid]}')
    #         if nums[mid] <= right:
    #             last_valid = mid
    #             low = mid + 1
    #         else:
    #             high = mid - 1
    #
    #     # Если есть допустимые j, добавляем их количество
    #     if first_valid <= last_valid:
    #         count += last_valid - first_valid + 1
    #     print()
    #
    # return count


# countFairPairs(nums = [0,1,7,4,4,5], lower = 3, upper = 6)