class Solution:
    '''
    Перевод задачи с LeetCode
    3394. Проверка возможности разрезать сетку на секции

    Уровень сложности: Средний

    Условие
    Дан размер n, представляющий размеры n × n сетки, где начало координат (0,0) находится в левом нижнем углу.

    Также дан двумерный массив rectangles, где:

    rectangles[i] = [startx, starty, endx, endy]
    Это прямоугольник на сетке с:
    (startx, starty) — нижний левый угол,
    (endx, endy) — верхний правый угол.
    🔹 Примечание: Прямоугольники не пересекаются.

    Нужно определить, можно ли разрезать сетку двумя горизонтальными или двумя вертикальными линиями так, чтобы:

    Получилось 3 секции, и каждая из них содержала хотя бы один прямоугольник.
    Каждый прямоугольник принадлежал ровно одной секции (не пересекал границы разреза).
    Верните true, если такие разрезы возможны, иначе false.

    Примеры
    Пример 1

    🔹 Вход:

    n = 4
    rectangles = [[1, 0, 3, 1], [0, 2, 4, 3], [2, 3, 3, 4]]
    🔹 Сетка (4×4) с прямоугольниками:

    . . . .  ← y = 3
    . █ █ .  ← y = 2
    █ █ █ █  ← y = 1
    . █ █ .  ← y = 0
    ────────
    0 1 2 3  ← x-координаты
    ✅ Возможный разрез по вертикали:

    |  . █ | █ .  |  ← y = 2
    |  █ █ | █ █  |  ← y = 1
    |  . █ | █ .  |  ← y = 0
    ──────────────
    0    1    2    3
    ✅ Разделение получилось!
    🔹 Выход: True
    '''
    def checkValidCuts(self, n: int, rectangles: list[list[int]]) -> bool:
        # проверяем горизонтальное разделение
        def horiz():
            y_s = [[i[1], i[3]] for i in rectangles]
            y_s.sort(key=lambda y:y[1])
            borders = [[k,v] for k,v in {i[0]:i[1] for i in y_s}.items()]
            return all([borders[i][1] <= borders[i + 1][1] for i in range(len(borders) - 1)])
        def vertic():
            x_s = [[i[0], i[2]] for i in rectangles] #нельзя переставлять?
            print(x_s)
            x_s.sort(key=lambda x:x[1])
            print(x_s)
            borders = [[k,v] for k,v in {i[0]:i[1] for i in x_s}.items()]
            return all([borders[i][1] <= borders[i + 1][1] for i in range(len(borders) - 1)])



        # print(horiz())
        print(vertic())
#



sol = Solution()
# sol.checkValidCuts(n = 5, rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]])
sol.checkValidCuts(n = 4, rectangles = [[0,0,1,1],[1,0,3,4],[0,2,2,3],[3,0,4,3]])