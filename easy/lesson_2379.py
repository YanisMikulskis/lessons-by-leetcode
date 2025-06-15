from collections import Counter
class Solution:
    '''
    Задача 2379: Минимальное перекрашивание для получения K подряд идущих черных блоков
    У вас есть строка blocks, состоящая из символов 'W' и 'B', где:

    'W' означает белый блок,
    'B' означает черный блок.
    Также вам дано число k, которое представляет желаемое количество подряд идущих черных блоков.

    За одну операцию вы можете перекрасить любой белый блок ('W') в черный ('B').

    Необходимо вернуть минимальное количество операций, требуемых для получения как минимум k
    подряд идущих черных блоков.

    Примеры
    Пример 1

    Входные данные:

    blocks = "WBBWWBBWBW", k = 7
    Выход:

    3
    Объяснение:
    Один из способов получить 7 подряд идущих черных блоков:
    Перекрасить blocks[3], blocks[4] и blocks[7], получим "WBBBBBBWBW".
    Для этого требуется 3 операции.
    '''

    def minimumRecolors(self, blocks: str, k: int) -> int:
        counter_blocks = Counter(blocks)

        border = 0
        slices = []
        for i in range(len(blocks)):
            slices.append(blocks[border:border + k])
            border += 1

        max_black, result_slise = 0, None
        for i in slices:
            count_B  = Counter(i)['B']
            if not count_B and not result_slise:
                if 'B' in blocks:
                    continue
                return k
            elif count_B == k:
                return 0
            elif count_B < k:
                if count_B > max_black:
                    max_black = count_B
                    result_slise = i
        else:
            return Counter(result_slise)['W']





sol = Solution()
# print(sol.minimumRecolors(blocks = "WBWW", k = 2))
# print(sol.minimumRecolors("WBBWWBBWBW", 7))
# print(sol.minimumRecolors("WBB", 1))
# print(sol.minimumRecolors("BW", 2))
# print(sol.minimumRecolors("WWBBW", 5))
# print(sol.minimumRecolors("WBWW", 2))
# print(sol.minimumRecolors("BWBW", 2))
# print(sol.minimumRecolors("WBWBBBW", 2))
print(sol.minimumRecolors("WBBWWWWBBWWBBBBWWBBWWBBBWWBBBWWWBWBWW", 15))
print(sol.minimumRecolors("WBB", 1))
# print(sol.minimumRecolors("WBWW", 2))
# print(sol.minimumRecolors("WBWW", 1))
# print(sol.minimumRecolors(blocks = "BB", k = 1))