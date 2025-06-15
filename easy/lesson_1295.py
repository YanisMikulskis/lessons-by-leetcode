# class Solution:
#     '''
#     📘 Задача: Найди числа с чётным количеством цифр
#
#     Уровень: Лёгкий
#     Описание:
#     Дан массив nums, состоящий из целых чисел. Верни количество тех чисел, которые содержат чётное количество цифр.
#
#     🔍 Примеры:
#     Пример 1:
#
#     Вход: nums = [12, 345, 2, 6, 7896]
#     Выход: 2
#
#     Пояснение:
#     12 → 2 цифры → чётное ✅
#     345 → 3 цифры → нечётное
#     2 → 1 цифра → нечётное
#     6 → 1 цифра → нечётное
#     7896 → 4 цифры → чётное ✅
#     → Итого: 2 числа с чётным количеством цифр
#     '''
#     def findNumbers(self, nums: list[int]) -> int:
#         return len([num for num in nums if len(str(num)) % 2 == 0])


# sol = Solution()
# print(sol.findNumbers(nums = [12, 345, 2, 6, 7896]))

from itertools import combinations

class Solution:
    '''
    Уровень сложности: 🔴 Сложная

    🧾 Условие:
    У тебя есть:

    n задач — каждая требует определённой силы (tasks[i])
    m работников — каждый имеет свою силу (workers[j])
    pills — магические таблетки, которые увеличивают силу работника
    strength — сила, на которую увеличивается сила одного работника после приёма таблетки
    🔹 Один работник может выполнить только одну задачу, если его сила не меньше требования задачи (worker >= task)

    🔹 Таблетку можно дать любому работнику, но не более одной на человека. Всего таблеток — pills.

    ✅ Цель:
    Найди максимальное количество задач, которые можно назначить работникам, с учётом возможности раздачи таблеток.

    🔍 Примеры:

    Пример 1:
    Вход:
    tasks = [3, 5, 8]
    workers = [7, 2, 4]
    pills = 1
    strength = 3

    Выход:
    2

    Пояснение:
    - Назначаем задачу с требованием 3 работнику с силой 4 → ок
    - Назначаем задачу с требованием 5 работнику с силой 2 + таблетка (2+3=5) → ок
    - Остался работник 7, но осталась только задача 8 → не может выполнить

    → Максимум 2 задачи
    '''
    def maxTaskAssign(self, tasks: list[int], workers: list[int], pills: int, strength: int) -> int:

        n = len(workers)
        all_variables = []
        tasks.sort()
        result = 0
        for positions in combinations(range(n), pills):
            super_workers = workers.copy()
            for pos in positions:
                super_workers[pos] += strength
            super_workers.sort()

            idx = 0
            good_workers = 0
            print(f'super worke')
            while idx < len(super_workers):
                if super_workers[idx] < min(tasks):
                    idx += 1
                    continue
                else:
                    for i in tasks:
                        if super_workers[idx] >= i:
                            good_workers += 1
                            break
                    idx += 1
            if good_workers > result:
                result = good_workers
                print(f'res = {result}   {super_workers}')


        print(f'result = {result}')





        print(all_variables)




sol = Solution()
sol.maxTaskAssign(tasks = [3, 5, 8], workers = [7, 2, 4], pills = 1, strength = 3)
sol.maxTaskAssign(tasks=[3,5,8,10,15], workers=[1,1,1,10,14], pills=1, strength=0)


