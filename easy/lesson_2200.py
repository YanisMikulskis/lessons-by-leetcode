class Solution:
    '''
    Вам дан целочисленный массив nums (нумерация с нуля) и два целых числа — key и k.

    Нужно найти все индексы i, для которых существует хотя бы один индекс j, удовлетворяющий двум условиям:

    |i - j| <= k (расстояние между i и j не больше k)
    nums[j] == key (на позиции j находится элемент key)
    Верните отсортированный по возрастанию список таких индексов i.

    🧪 Примеры:
    Пример 1:

    nums = [3, 4, 9, 1, 3, 9, 5]
    key = 9
    k = 1
    🔍 Пояснение:

    Индексы, где nums[j] == 9: j = 2 и j = 5
    Ищем все i, такие что |i - j| <= 1
    Для j = 2: допустимы i = 1, 2, 3
    Для j = 5: допустимы i = 4, 5, 6
    📌 Ответ: [1, 2, 3, 4, 5, 6]
    '''
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        if len(set(nums)) == 1:
            return list(range(len(nums)))
        idxes = [idx for idx in range(len(nums)) if nums[idx] == key]
        res = []
        for j in idxes:
            res += [i for i in range(len(nums)) if abs(i - j) <= k and i not in res]


        # print(idxes)
        print(res)
        return res

sol = Solution()
print(sol.findKDistantIndices(nums = [3,4,9,1,3,9,5], key = 9, k = 1))
print(sol.findKDistantIndices(nums = [2,2,2,2,2], key = 2, k = 2))