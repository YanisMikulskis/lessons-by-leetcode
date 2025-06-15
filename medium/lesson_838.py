class Solution:
    '''
    🧩 Условие задачи: Падающие доминошки

    У тебя есть строка dominoes длиной n, в которой каждое значение — это одно домино, стоящее в ряд.
     Все домино изначально стоят вертикально. Затем одновременно некоторые из них начинают падать влево (L)
     или вправо (R).

    Правила падения:

    Если домино падает вправо (R), через 1 секунду оно толкает следующее справа стоящее домино.
    Если домино падает влево (L), через 1 секунду оно толкает следующее слева стоящее домино.
    Если на одно вертикальное домино одновременно действуют силы справа (L) и слева (R), оно остаётся стоять (.),
    т.к. силы уравновешены.
    ⚠️ Замечание: домино, уже падающее или упавшее, не мешает другим продолжать падение.

    🔄 Задача:

    По заданной строке dominoes, представляющей начальное состояние (R, L, .), вернуть строку,
     представляющую конечное состояние всех домино.

    🧪 Примеры:

    Пример 1:
    Ввод:

    dominoes = "RR.L"
    Вывод:

    "RR.L"
    Пояснение:

    Первые два R уже падают вправо, но третий — уже L, то есть он падает влево, и их влияние
    друг на друга не пересекается. Никаких изменений не произойдёт.


    Пример 2:
    Ввод:

    dominoes = ".L.R...LR..L.."
    Вывод:

    "LL.RR.LLRRLL.."
    Пояснение:

    . между L и R остаётся стоять, т.к. они не сталкиваются.
    ... между L и R в центре — под действием обеих сторон, в середине останется ..
    '''
    def pushDominoes(self, dominoes: str) -> str:
        ...
        idx = 0
        temporary_points = []
        border_after = []
        result = []
        bord = 0
        dominoes = list(dominoes)
        for i in range(len(dominoes)):
            if i < len(dominoes) - 1:
                if dominoes[i] == 'L' or dominoes[i] == 'R':

                    part = dominoes[bord:i + 1]
                    # if '.' not in part:
                    #     continue
                    part_copy = part.copy()
                    border_after.append(part_copy)
                    print(f'part = {part}')

                    if part[0] == '.':
                        part = list(part[-1] * len(part)) if part[-1] == 'L' else part

                    elif part[-1] == '.':
                        part = list(part[-1] * len(part)) if part[-1] == 'R' else part


                    elif part[0] == part[-1]:
                        part = list(part[0] * len(part))

                    else:

                        if len(part[1:-1]) % 2 != 0:
                            for item in range(len(part) // 2):
                                if part[item] == 'R':
                                    if part[item + 2] != 'L':
                                        part[item + 1] = 'R'

                                if part[-item - 1] == 'L':
                                    if part[-item - 3] != 'R':
                                        part[-item - 2] = 'L'
                        else:
                            part[:len(part) // 2] = list('R' * (len(part) // 2))
                            part[len(part) // 2:] = list('L' * (len(part) // 2))
                    result.append(part)
                    bord = i
            else:
                border_after.append(dominoes[bord:i + 1])
                result.append(dominoes[bord:])



        print(f'after = {border_after}')
        print(f'before = {result}')


        # new_res = []
        # for i in range(len(result) - 1):
        #     if result[i + 1][0] == result[i][-1]:
        #         new_res.append(result[i][:-1])
        #     else:
        #         new_res.append(result[i])
        # else:
        #     new_res.append(result[i])



        # print(f'new res = {new_res}')
        # new_res = []
        # for i in range(len(result)):
        #     if i < len(result) - 1:
        #         if i % 2 != 0:
        #             new_res.append(result[i][1:-1])
        #         else:
        #             new_res.append(result[i])
        #     else:
        #         new_res.append(result[i][1:])
        # print(f'new res = {new_res}')
        # result = list(map(lambda x: x[1:], result))
        # result = [result[i][1:-1] if i > 0 and i % 2 != 0 else result[i] for i in range(len(result))]
        # result = ''.join(list(map(lambda x:''.join(x), result)))
        # new_result = []
        # for i in range(len(result)):
        #     if i > 0 and i % 2 != 0:
        #         result.append(result[i][1:-1])
        #     else:
        #         result.append(result[i])
        # print(f'resultt = {result}')



sol = Solution()
sol.pushDominoes(dominoes = ".L.R...LR..L..")   #"LL.RR.LLRRLL.."
# sol.pushDominoes(dominoes='R..R.L.LR.')
# sol.pushDominoes(dominoes='.........L.R...L')
sol.pushDominoes(dominoes='..R......L.R...L')
# sol.pushDominoes('RR.L')

# print(f'new_string = {new_string}')

# s = list(".L.R...LR..L..")
# new_str = []
# bord = 0
# for i in range(len(s)):
#     if s[i] in ['L', 'R']:
#         new_str.append(s[bord:i + 1])
#         bord = i
# print(f'new str = {new_str}')