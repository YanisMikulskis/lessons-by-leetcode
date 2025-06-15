class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        '''
        Вам дана двумерная целочисленная матрица grid размером n × n, индексируемая с нуля (0-indexed).

        Все значения в матрице находятся в диапазоне [1, n²].
        Каждое число встречается ровно один раз, за исключением числа a, которое повторяется дважды, и числа b, которое отсутствует.
        Ваша задача — найти повторяющееся число a и отсутствующее число b.
        Формат вывода
        Верните массив ans длины 2, где:

        ans[0] — повторяющееся число a,
        ans[1] — отсутствующее число b.
        Примеры
        Пример 1

        Вход:
        grid = [[1, 3],
                [2, 2]]
        Выход:
        [2, 4]
        Объяснение:
        Число 2 повторяется.
        Число 4 отсутствует.
        Ответ: [2, 4].
        '''
        module = __import__('collections')
        all_elements = [j for i in grid for j in i]
        counters = module.Counter(all_elements)
        repeat = [rep for rep in counters if counters[rep] == 2]
        missing = set(list(range(1, len(grid) ** 2 + 1))) ^ set(all_elements)

        return [*repeat, *missing]

sol = Solution()
print(sol.findMissingAndRepeatedValues(grid = [[9, 1, 7],
                                        [8, 9, 2],
                                        [3, 4, 6]]))