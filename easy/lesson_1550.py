class Solution:
    '''
    Условие задачи:
    Дан целочисленный массив arr. Верните true, если в массиве есть три подряд идущих нечетных числа.
    В противном случае верните false.

    Примеры:

    Пример 1:

    python
    Вход: arr = [2, 6, 4, 1]
    Выход: false
    Объяснение: В массиве нет трех последовательных нечетных чисел.

    Пример 2:

    python
    Вход: arr = [1, 2, 34, 3, 4, 5, 7, 23, 12]
    Выход: true
    Объяснение: В массиве есть последовательность [5, 7, 23] - три нечетных числа подряд.

    '''

    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        ans = 0
        for num in arr:
            ans = ans + 1 if num % 2 != 0 else 0
            if ans == 3:
                return True
        return False


sol = Solution()
print(sol.threeConsecutiveOdds(arr = [1, 2, 34, 3, 4, 5, 7, 23, 12]))