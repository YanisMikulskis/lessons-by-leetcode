class Solution:
    '''
    Задача:
    Дан строка s и число k. Нужно разделить строку s на k подстрок таким образом, чтобы как можно
    меньше операций изменения символов потребовалось для того, чтобы все подстроки стали палиндромами.
    Вопрос: сколько минимальных изменений нужно сделать, чтобы строка была разделена на k палиндромных подстрок.

    Описание:
    Палиндром — это строка, которая читается одинаково слева направо и справа налево.
    Необходимо разделить строку s на k подстрок, при этом минимизировать количество изменений,
    чтобы каждая подстрока стала палиндромом.
    Входные данные:

    Строка s длиной от 1 до 1000 символов.
    Целое число k, 1 ≤ k ≤ len(s).
    Выходные данные:

    Возвращаем минимальное количество изменений, которые нужно сделать для получения k палиндромных подстрок.
    '''
    def palindromePartition(self, s: str, k: int) -> int:
        if k == len(s):
            return 0
        dp = []


sol = Solution()
print(sol.palindromePartition(
    s = 'abc',
    k = 3
))


print(sol.palindromePartition(s = "aabbc", k = 3)) #a a bbc    a abb c     a ab bc   aab b c    aa bb c
