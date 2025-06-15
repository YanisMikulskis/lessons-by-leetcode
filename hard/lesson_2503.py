class Solution:
    '''
    Задача:
    Дана целочисленная матрица grid размером m × n и массив queries размера k.

    Требуется найти массив answer размера k, где answer[i] определяется следующим процессом:

    Вы начинаете в верхней левой ячейке (grid[0][0]).
    Если queries[i] строго больше текущего значения ячейки, то:
    Получаете 1 очко, если впервые посещаете эту ячейку.
    Можете перейти в любую из 4-х соседних ячеек (вверх, вниз, влево, вправо).
    Если queries[i] не больше значения текущей ячейки, то процесс останавливается.
    В конце answer[i] — это максимальное количество очков, которое можно заработать для queries[i].
    Примеры:
    Пример 1

    Вход:

    grid = [[1,2,4],[3,4,3],[2,1,2]]
    queries = [2, 3, 4]
    Выход:

    [2, 5, 8]
    Объяснение:

    Для queries[0] = 2:
    grid[0][0] = 1 (меньше 2) → +1 очко
    grid[0][1] = 2 (не меньше 2) → Остановка, всего 2 очка
    Для queries[1] = 3:
    Можно пройти больше клеток, всего 5 очков
    Для queries[2] = 4:
    Можно пройти все 8 клеток
    '''
    def maxPoints(self, grid: list[list[int]], queries: list[int]) -> list[int]:
        answer = []
        idx = 0
        for i in grid:
            print(i)
        for number in queries:





            def func(line, point, res):
                print(grid[line][point])
                if grid[line][point] < number:
                    res += 1
                    if line < len(grid) - 1:
                        func(line + 1, point, res)
                    else:


                else:
                    return

            func(0, 0, 0)

        # sosedi = []
        # for i in grid:
        #     print(i)
        # for i in range(len(grid)):
        #     for j in range(len(grid[i])):
        #         sosedi.append([grid[i][j], []])
        #         if i == 0:
        #             if j == 0:
        #                 sosedi[-1][-1].append(grid[i][j + 1])
        #             elif len(grid[i]) - 1 > j > 0:
        #                 sosedi[-1][-1].append(grid[i][j + 1])
        #                 sosedi[-1][-1].append(grid[i+1][j])
        #                 sosedi[-1][-1].append(grid[i][j - 1])
        #             else:
        #                 sosedi[-1][-1].append(grid[i][j - 1])
        #                 sosedi[-1][-1].append(grid[i + 1][j])
        #         elif len(grid) - 1 > i > 0:
        #             if j == 0:
        #                 sosedi[-1][-1].append(grid[i-1][j])
        #                 sosedi[-1][-1].append(grid[i][j + 1])
        #                 sosedi[-1][-1].append(grid[i + 1][j])
        #             elif len(grid[i]) - 1 > j > 0:
        #                 sosedi[-1][-1].append(grid[i - 1][j])
        #                 sosedi[-1][-1].append(grid[i][j + 1])
        #                 sosedi[-1][-1].append(grid[i][j - 1])
        #                 sosedi[-1][-1].append(grid[i + 1][j])
        #             else:
        #                 sosedi[-1][-1].append(grid[i - 1][j])
        #                 sosedi[-1][-1].append(grid[i][j - 1])
        #                 sosedi[-1][-1].append(grid[i + 1][j])
        #         else:
        #             if j == 0:
        #                 sosedi[-1][-1].append(grid[i - 1][j])
        #                 sosedi[-1][-1].append(grid[i][j+1])
        #             elif len(grid[i]) - 1 > j > 0:
        #                 sosedi[-1][-1].append(grid[i - 1][j])
        #                 sosedi[-1][-1].append(grid[i][j - 1])
        #                 sosedi[-1][-1].append(grid[i][j + 1])
        #             else:
        #                 sosedi[-1][-1].append(grid[i][j - 1])
        #                 sosedi[-1][-1].append(grid[i - 1][j])
        # print(sosedi)


sol = Solution()
sol.maxPoints(grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2])