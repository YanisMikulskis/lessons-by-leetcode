class Solution:
    '''
    Вам дан целочисленный массив nums.
    Вы можете удалить любое количество элементов из массива,
    при этом массив не должен становиться пустым. После выполнения удалений выберите подмассив массива таким образом, чтобы:

    Все элементы в подмассиве были уникальными.
    Сумма элементов подмассива была максимальной.
    Верните максимальную сумму такого подмассива.
    Пример 1:
    Ввод:

    nums = [4, 2, 4, 5, 6]
    Объяснение:

    После удаления второго числа (4), подмассив [2, 4, 5, 6] содержит уникальные элементы.
    Сумма этого подмассива: 2 + 4 + 5 + 6 = 17.
    Вывод:

    17
    '''
    def maxSum(self, nums: list[int]) -> int:

        new_arr = []

        for i in nums:
            if i not in new_arr:
                new_arr.append(i)
        dict_sols = {

        }
        if all([i > 0 for i in new_arr]):
            return sum(new_arr)

        elif all([i < 0 for i in new_arr]):
            return max(new_arr)

        elif any([i >= 0 for i in new_arr]):
            return sum([i for i in new_arr if i >= 0])

        elif len(new_arr) == 1:
            return new_arr[0]



sol = Solution()
print(sol.maxSum(nums = [4, 2, 4, 5, 6]))
print(sol.maxSum(nums = [1, 2, 3, 1, 2, 3]))
print(sol.maxSum(nums = [1,2,-1,-2,1,0,-1]))
print(sol.maxSum(nums = [-17,-15]))
print(sol.maxSum([-15,0]))


