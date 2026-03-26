class Solution:
    '''
    Дана двоичная строка s и целое число k. Верните true, если каждая двоичная комбинация (код) длины k является подстрокой s. В противном случае верните false.
    Примеры

    Пример 1:
    Входные данные: s = "00110110", k = 2
    Выходные данные: true
    Пояснение: Двоичные коды длины 2: "00", "01", "10" и "11". Их можно найти как подстроки:

    "00" — с индекса 0
    "01" — с индекса 1
    "10" — с индекса 2 (и с индекса 5)
    "11" — с индекса 3
    '''
    def hasAllCodes(self, s: str, k: int):
        d = {s[j:j+k]:1 for j in range(len(s))}
        for i in range(2**k):
            b = bin(i)[2:]
            bin_number = '0' * (k - len(b)) + b
            try:
                if d[bin_number]:
                    continue
            except KeyError:
                return False
        return True


sol = Solution()
print(sol.hasAllCodes(s = '00000000001011100', k = 3))
# print(sol.hasAllCodes(s = "12345678", k = 2))