class Solution:
    '''
    2523. Ближайшие простые числа в диапазоне
    Тебе даны два целых числа left и right, которые задают диапазон [left, right] (включительно).
    Твоя задача — найти две различных простых числа в этом диапазоне, которые находятся на минимальном
    расстоянии друг от друга.

    Если в диапазоне есть несколько пар с одинаковым минимальным расстоянием, выбери пару с наименьшими числами.
    Если в диапазоне нет хотя бы двух простых чисел, верни [-1, -1].
    '''
    def closestPrimes(self, left: int, right: int) -> list[int]:
        if left == right:
            return [-1,-1]
        sieve = list(range(2, right + 1))
        check, last_el, border = 2, sieve[-1], 0
        while check ** 2 <= last_el:

            for i in range(border, len(sieve), check):
                sieve[i] = False if sieve[i] != check else sieve[i]

            for i in range(len(sieve)):
                if sieve[i] and sieve[i] > check:
                    check, border = sieve[i], i
                    break
        print(sieve)
        result = [i for i in sieve if i >= left]
        print(result)
        print()
        if len(result) < 2:
            return [-1,-1]
        delta = [[[result[i], result[i + 1]], result[i + 1] - result[i]] for i in range(len(result) - 1)]
        return min(delta, key=lambda x:x[1])[0]







sol = Solution()
# print(sol.closestPrimes(10, 19))
print(sol.closestPrimes(21, 25))