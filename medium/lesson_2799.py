from collections import Counter
class Solution:
    '''
    Дан массив nums, состоящий из положительных целых чисел.

    Подмассив называется полным, если:

    количество различных элементов в этом подмассиве равно количеству различных элементов во всём массиве.
    Найди и верни количество полных подмассивов в nums.

    📌 Подмассив — это непустой, непрерывный фрагмент массива.

    ✅ Примеры:
    Пример 1:

    Вход: nums = [1, 3, 1, 2, 2]
    🔍 Весь массив содержит 3 уникальных элемента: {1, 2, 3}
    Полные подмассивы (в которых тоже 3 уникальных числа):

    [1, 3, 1, 2]
    [1, 3, 1, 2, 2]
    [3, 1, 2]
    [3, 1, 2, 2]
    📤 Выход: 4


    '''
    def countCompleteSubarrays(self, nums: list[int]) -> int:

        if max(Counter(nums).values()) == len(nums):
            res = 0
            for i in range(1, len(nums) + 1):
                res += i
            return res

        uniq_elements = len(set(nums))
        result = 0
        for i in range(len(nums)):
            for j in range(i + uniq_elements - 1, len(nums)):
                subarray = nums[i:j + 1]
                if len(set(subarray)) == uniq_elements:
                    result += 1
        return result
sol = Solution()
# sol.countCompleteSubarrays([5,5,5,5])
sol.countCompleteSubarrays(nums = [1,3,1,2,2])