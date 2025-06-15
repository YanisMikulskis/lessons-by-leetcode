class Solution:
    '''
    На круге расположены плитки красного и синего цветов. Вам дан массив целых чисел colors и целое число k. Цвет плитки с индексом i представлен значением colors[i]:

    colors[i] == 0 означает, что плитка красная.
    colors[i] == 1 означает, что плитка синяя.
    Альтернирующая группа — это каждые k подряд идущих плиток на круге, цвета которых чередуются (каждая плитка в группе, кроме первой и последней, должна отличаться по цвету от своих левой и правой соседних плиток).

    Поскольку плитки образуют круг, первая и последняя плитки считаются соседними.

    Необходимо вернуть количество альтернирующих групп.

    Примеры:

    Пример 1:

    Ввод:

    python
    Copy
    colors = [0, 1, 0, 1, 0], k = 3
    Вывод:

    python
    Copy
    4
    Объяснение:
    Возможные альтернирующие группы:

    Плитки с индексами 0, 1, 2: [0, 1, 0].
    Плитки с индексами 1, 2, 3: [1, 0, 1].
    Плитки с индексами 2, 3, 4: [0, 1, 0].
    Плитки с индексами 3, 4, 0: [1, 0, 1].
    '''
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        # all_alt = []
        # test_lst = [1,2,3,4] #[4,1,2,3], [3,4,1,2], [2,3,4,1]
        # perms = []
        # for i in range(len(test_lst)):
        #     test_lst = [test_lst[-1]] + test_lst[:-1]
        #     perms.append(test_lst)
        # print(perms)
        # perms = []
        #
        alternats = [False] * len(colors)
        print(alternats)
        for i in range(len(colors)):
            alternats[i] = (colors[i - 1] != colors[i])






        # cnt = 0
        # def check_alt(lst):
        #     first_el = lst[0]
        #     for i in lst[1:]:
        #         if i == first_el:
        #             return False
        #         else:
        #             first_el = i
        #     return True
        #
        # for i in range(len(colors)):
        #     if i + k > len(colors):
        #         if check_alt(colors[i:] + colors[:(i + k) - len(colors)]):
        #             cnt += 1
        #     else:
        #         if check_alt(colors[i:i + k]):
        #             cnt += 1


        # return cnt

        #
        # idx = 0
        # cnt = 1
        # ans = 0
        # while idx < len(colors):
        #     if colors[idx] != colors[idx + 1]:
        #         cnt += 1
        #     else:
        #         if cnt == k:
        #             ans += 1
        #         else:
        #             cnt = 0
        #


sol = Solution()
# print(sol.numberOfAlternatingGroups(colors = [1, 2, 3, 4, 5], k = 4))
print(sol.numberOfAlternatingGroups(colors = [0,1,0,1,0], k = 3))
# print(sol.numberOfAlternatingGroups(colors = [0,1,0,0,0,1,0], k = 3))




