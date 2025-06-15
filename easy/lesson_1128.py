from collections import Counter
from itertools import combinations
class Solution:
    '''
    Условие задачи:
    Дан список домино, где каждый элемент dominoes[i] = [a, b]. Два домино [a, b] и [c, d] считаются эквивалентными, если:

    a == c и b == d, или
    a == d и b == c (то есть одно домино можно перевернуть, чтобы оно совпало с другим).
    Необходимо найти количество пар индексов (i, j) таких, что 0 <= i < j < длина(dominoes) и dominoes[i] эквивалентно dominoes[j].

    Примеры:

    Пример 1:

    Вход:

    python
    dominoes = [[1,2], [2,1], [3,4], [5,6]]
    Выход: 1
    Объяснение:

    Эквивалентна только одна пара: [1,2] и [2,1] (так как [2,1] можно перевернуть в [1,2]).
    Остальные домино ([3,4], [5,6]) не имеют эквивалентных пар.

    '''
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        cnt = {

        }
        for i in list(map(tuple, dominoes)):
            rev_i = tuple(list(i)[::-1])
            if rev_i in cnt:
                cnt[rev_i] += 1
                continue
            else:
                cnt.setdefault(i,0)
            cnt[i] += 1

        result = 0
        for k,v in cnt.items():
            if v > 1:
                result += v * (v - 1) // 2
        return result








sol = Solution()
sol.numEquivDominoPairs(dominoes = [[1,2],[2,1],[3,4],[5,6]])
sol.numEquivDominoPairs(dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]])
