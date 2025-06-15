class Solution:
    '''
    Описание задачи:
    Вам дан целочисленный массив nums длины n и двумерный массив queries, где queries[i] = [l_i, r_i, val_i].
    Каждый элемент queries[i] представляет собой следующее действие над массивом nums:
    Уменьшить значение каждого элемента в диапазоне индексов [l_i, r_i] массива nums не более чем на val_i.
    Величина уменьшения для каждого индекса может быть выбрана независимо.
    Нулевой массив — это массив, в котором все элементы равны 0.

    Необходимо вернуть минимальное возможное неотрицательное значение k,
    такое что после обработки первых k запросов по порядку, массив nums становится нулевым.
     Если такого k не существует, вернуть -1.

    Пример 1:
    Входные данные:

    nums = [2, 0, 2]
    queries = [[0, 2, 1], [0, 2, 1], [1, 1, 3]]
    Выходные данные:

    2
    Пояснение:

    Запрос 0: l = 0, r = 2, val = 1
    Уменьшаем значения в индексах [0, 1, 2] на [1, 0, 1] соответственно.
    Массив становится [1, 0, 1].
    Запрос 1: l = 0, r = 2, val = 1
    Уменьшаем значения в индексах [0, 1, 2] на [1, 0, 1] соответственно.
    Массив становится [0, 0, 0], что является нулевым массивом.
    Таким образом, после применения первых двух запросов, массив nums становится нулевым.


    '''
    def minZeroArray(self, nums: list[int], queries: list[list[int]]) -> int:
        ans = 0
        queries = [list(range(query[0], query[1] + 1)) + [query[2]] for query in queries]
        def check_zero():
            if nums.count(0) == len(nums):
                return 0 if not ans else ans
        check_zero()
        for que in queries:
            inc = que[-1]
            for el in que[:-1]:
                if el == len(nums):
                    if nums[el] == 0:

                        return 0
                    break
                if nums[el] == 0:

                    pass
                elif nums[el] <= inc:
                    nums[el] -= nums[el]
                else:
                    nums[el] -= inc
            else:
                ans += 1

            if nums.count(0) == len(nums):
                return ans
        return -1


sol = Solution()
# print(sol.minZeroArray([2, 0, 2], [[0, 2, 1], [0, 2, 1], [1, 1, 3]]))
# print(f'---')
# print(sol.minZeroArray([1,2,3], [[0, 1, 1], [1, 2, 1], [0, 2, 1]]))
# print('f----')
# print(sol.minZeroArray([0], [[0, 1, 1], [0, 2, 1], [0, 2, 1]]))
print(sol.minZeroArray([0],[[0,0,2],[0,0,4],[0,0,4],[0,0,3],[0,0,5]]))