class Solution:
    '''Условие задачи:
    Вам дан массив целых чисел nums длины n и двумерный массив queries, где queries[i] = [li, ri].

    Каждый queries[i] обозначает следующее действие:

    Выберите подмножество индексов в диапазоне [li, ri].
    Уменьшите значения на этих выбранных индексах на 1.
    Нулевой массив — это массив, в котором все элементы равны 0.

    Задача:

    Верните true, если можно, выполняя все запросы по порядку, превратить nums в нулевой массив.
    Иначе верните false.

    🔍 Примеры
    Пример 1:

    Вход:
    nums = [1, 0, 1]
    queries = [[0, 2]]

    Выход:
    true

    Пояснение:
    Выбираем индексы 0 и 2 в запросе [0,2] и уменьшаем их значения на 1.
    Массив становится: [0, 0, 0] — это нулевой массив.
    Пример 2:

    Вход:
    nums = [4, 3, 2, 1]
    queries = [[1, 3], [0, 2]]

    Выход:
    false

    Пояснение:

    1. Запрос [1, 3]: уменьшаем индексы 1, 2 и 3 → массив: [4, 2, 1, 0]
    2. Запрос [0, 2]: уменьшаем индексы 0, 1, 2 → массив: [3, 1, 0, 0]

    В результате остались ненулевые элементы (3 и 1), значит массив — **не нулевой**.
    Если нужно, могу объяснить идею решения или показать код.
    '''

    def isZeroArray(self, nums: list[int], queries: list[list[int]]) -> bool:
        # nums = list(map(list, enumerate(nums)))
        # for query in queries:
        #     interval = list(range(query[0], query[1] + 1))
        #     nums = list(
        #         map(lambda x: [x[0], x[1] - 1 if x[1] > 0 else x[1]] if x[0] in interval else [x[0], x[1]], nums))
        # else:
        #     if all(list(map(lambda x: x[1] == 0, nums))):
        #         return True
        #     return False





        # queries_dict = {
        #
        # }
        #
        # for i in queries:
        #
        #     for j in range(i[0], i[1] + 1):
        #         if j not in queries_dict:
        #             queries_dict[j] = 0
        #         queries_dict[j] += 1
        #
        # for idx,cnt in queries_dict.items():
        #     print(f'nums = {nums}')
        #     nums[idx] -= cnt
        #     nums[idx] = 0 if nums[idx] <= 0 else nums[idx]
        # return all(map(lambda x: x == 0, nums))

        deltaArray = [0] * (len(nums) + 1)
        print(deltaArray)
        for left, right in queries:
            deltaArray[left] += 1
            deltaArray[right + 1] -= 1
        print(deltaArray)
        print(f'---')
        operationCounts = []
        currentOperations = 0
        for delta in deltaArray:
            currentOperations += delta
            operationCounts.append(currentOperations)

        print(operationCounts)
        print(list(zip(operationCounts, nums)))
        for operations, target in zip(operationCounts, nums):
            print(f'op = {operations}')
            print(f'tr = {target }')

            if operations < target:
                return False
        return True



sol = Solution()
# print(sol.isZeroArray(nums = [4,3,2,1], queries = [[1,3],[0,2]]))
print(sol.isZeroArray(nums=[1, 0, 1], queries=[[0, 2]]))
# print(sol.isZeroArray(nums=[6, 0, 1], queries=[[2, 2]]))

# print(sol.isZeroArray([1,2,3,4], [[1,3], [2,4]]))
