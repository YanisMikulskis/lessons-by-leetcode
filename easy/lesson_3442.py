from collections import Counter
class Solution:
    '''
    Задача (перевод):
    Дана строка s, состоящая из строчных английских букв.
    Ваша задача — найти максимальную разницу diff = freq(a1) - freq(a2) между частотами двух
    символов a1 и a2 в строке, при условии, что:
    a1 встречается в строке с нечётной частотой.
    a2 встречается в строке с чётной частотой.
    Верните максимально возможное значение этой разницы.
    Примеры:
    Пример 1:
    plaintext
    Копировать код
    s = "aabbcc"
    Частоты:
    a: 2 (чётная)
    b: 2 (чётная)
    c: 2 (чётная)
    a1 должен иметь нечётную частоту, значит, возможных a1: нет, так как все частоты чётные.
    Следовательно, максимум невозможен, ответ — 0 или минимальное значение по условию (зависит от реализации).
    Ответ: 0
    '''
    def maxDifference(self, s: str) -> int:
        cnt = Counter(s)
        def freq(parity):
            return [cnt[sym] for sym in cnt if (cnt[sym] % 2 != 0 if not parity else cnt[sym] % 2 == 0)]
        a1_lc, a2_lc = freq(False), freq(True)
        if not a1_lc or not a2_lc:
            return 0
        return max(a1_lc) - min(a2_lc)

sol = Solution()
# print(sol.maxDifference("aaaaabbc"))
# print(sol.maxDifference("aabbcc"))
print(sol.maxDifference("mmsmsym"))