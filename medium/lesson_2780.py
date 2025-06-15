from collections import Counter
class Solution:
    '''
    Перевод задачи с LeetCode 2780: Минимальный индекс допустимого разбиения
    Условие:
    Элемент x массива целых чисел arr длины m называется доминирующим, если более половины элементов массива равны x.

    Дан 0-индексированный массив целых чисел nums длины n, содержащий ровно один доминирующий элемент.

    Вы можете разрезать nums в позиции i, получая два подмассива:

    nums[0, ..., i]
    nums[i + 1, ..., n - 1]
    Разбиение считается допустимым, если выполняются оба условия:

    0 <= i < n - 1
    Оба полученных подмассива имеют тот же доминирующий элемент, что и исходный массив.
    Верните минимальный индекс i, при котором разбиение является допустимым.
    Если такого разбиения не существует, верните -1.

    Примеры:
    Пример 1

    Вход:

    nums = [1,2,2,2]
    Выход:

    2
    Объяснение:

    Доминирующий элемент — 2 (он встречается в 3 из 4 элементов).
    Возможные разбиения:
    i = 0: [1] | [2,2,2] → 2 не доминирует в первом массиве.
    i = 1: [1,2] | [2,2] → 2 не доминирует в первом массиве.
    i = 2: [1,2,2] | [2] → 2 доминирует в обоих частях. ✅
    Минимальный допустимый индекс разбиения — 2.
    '''
    def minimumIndex(self, nums: list[int]) -> int:
        def find_dominator(lst):
            counter_lists = Counter(lst)
            max_count = max(counter_lists, key=counter_lists.get)
            dominator = max_count if counter_lists[max_count] / len(lst) > 0.5 else -1
            return dominator
        general_dominator = find_dominator(nums)
        for i in range(1, len(nums)):
            left_dominator, right_dominator = find_dominator(nums[:i]), find_dominator(nums[i:])
            if left_dominator == right_dominator == general_dominator:
                return i - 1
        return -1






sol = Solution()
# sol.minimumIndex(nums = [2,1,3,1,1,1,7,1,2])
print(sol.minimumIndex(nums = [3, 3, 3, 3, 7, 2, 2]))
print(sol.minimumIndex(nums = [1,2,2,2]))
print(sol.minimumIndex([2,1,3,1,1,1,7,1,2,1]))