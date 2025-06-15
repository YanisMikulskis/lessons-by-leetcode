class Solution:
    '''
    Задача: Максимальное количество контейнеров на корабле
    Вам дано положительное целое число n, представляющее n × n грузовую палубу на корабле.
    Каждая ячейка палубы может вместить один контейнер весом w.
    Однако общий вес всех загруженных контейнеров не должен превышать максимальную грузоподъёмность корабля maxWeight.
    Верните максимальное количество контейнеров, которое можно разместить на корабле, соблюдая ограничения по весу.

    Примеры (с LeetCode):
    Пример 1:
    Вход:
    n = 3
    w = 2
    maxWeight = 10

    Выход:
    5
    Объяснение:
    Максимально возможное количество контейнеров на палубе — 3 × 3 = 9, но их общий вес будет 9 × 2 = 18,
    что превышает maxWeight = 10.
    Поэтому можно загрузить только 5 контейнеров, чтобы их суммарный вес был не больше 10.
    '''
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        max_dockers = n * n
        max_w_dockers = max_dockers * w

        if max_w_dockers < maxWeight:
            return max_w_dockers // w
        while max_w_dockers > maxWeight:
            max_w_dockers -= w


        return max_w_dockers // w




sol = Solution()
# print(sol.maxContainers(n = 4, w = 3, maxWeight = 20))
#
# print(sol.maxContainers(n = 3, w = 2, maxWeight = 10))
print(sol.maxContainers(n = 2, w = 3, maxWeight=15))