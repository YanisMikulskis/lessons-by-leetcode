class Solution:
    '''
    Даны три положительных целых числа: zero, one и limit.

    Бинарный массив arr называется стабильным, если:

    Количество вхождений 0 в arr равно zero.
    Количество вхождений 1 в arr равно one.
    Каждый подмассив arr размером больше limit содержит и 0, и 1.
    Верните общее количество стабильных бинарных массивов.

    Так как ответ может быть очень большим, верните его по модулю

    '''
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        ...

sol = Solution()
sol.numberOfStableArrays()