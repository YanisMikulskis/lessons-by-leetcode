from collections import Counter
class Solution:
    '''
    Дан целочисленный массив nums длины n (индексация с нуля) и целое число k.

    Нужно найти количество пар индексов (i, j), таких что:

    0 <= i < j < n
    nums[i] == nums[j] (значения на этих позициях одинаковые)
    (i * j) % k == 0 (произведение индексов делится на k без остатка)
    🔢 Примеры:

    ▶ Пример 1:
    Вход: nums = [3, 1, 2, 2, 2, 1, 3], k = 2
    Выход: 4
    ✅ Подходящие пары:

    (0, 6) → nums[0] == nums[6] == 3, и 0 * 6 = 0, делится на 2
    (2, 3) → nums[2] == nums[3] == 2, и 2 * 3 = 6, делится на 2
    (2, 4) → nums[2] == nums[4] == 2, и 2 * 4 = 8, делится на 2
    (3, 4) → nums[3] == nums[4] == 2, и 3 * 4 = 12, делится на 2
    '''
    def countPairs(self, nums: list[int], k: int) -> int:
        if max(Counter(nums).values()) == 1:
            return 0
        couples = 0

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and (i * j) % 2 == 0:
                    couples += 1
        return couples


        # nums = list(enumerate(nums))

        # temp_dict = {
        #
        # }
        # for i in range(len(nums)):
        #     if nums[i] not in temp_dict:
        #         temp_dict.setdefault(nums[i], [i])
        #
        # print(nums)

        # left, right = 0, 1
        # cow = 0
        # while left != len(nums) - 2:
        #     if right == len(nums):
        #         left += 1
        #         right = left + 1
        #     if nums[left] == nums[right] and (left * right) % k == 0:
        #         cow += 1
        #     right += 1
        # else:
        #     if len(nums) == 2 and len(set(nums)) == 1:
        #         return 1
        # return cow




sol = Solution()
print(sol.countPairs(nums = [3, 1, 2, 2, 2, 1, 3], k = 2))
print(sol.countPairs([7,7], 7))
# sol.countPairs(nums = [1, 2, 3, 4], k = 1)