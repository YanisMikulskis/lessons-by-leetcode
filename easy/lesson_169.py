from collections import Counter
class Solution:
    '''
    169. Элемент большинства
    Уровень сложности: Лёгкий

    Дан массив nums размера n. Необходимо вернуть элемент большинства.

    Элементом большинства называется элемент, который встречается более чем ⌊n / 2⌋ раз.
    Можно считать, что такой элемент всегда существует в массиве.

    Примеры:
    Пример 1:
    Вход: nums = [3, 2, 3]
    Выход: 3

    Пример 2:
    Вход: nums = [2, 2, 1, 1, 1, 2, 2]
    Выход: 2
    '''
    def majorityElement(self, nums: list[int]) -> int:
        cnt = Counter(nums)
        return max(cnt, key=lambda x: cnt[x])
sol = Solution()
print(sol.majorityElement([2,2,1,1,1,2,2, 0, 0, 0, 0, 0, 0]))