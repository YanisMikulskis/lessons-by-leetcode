class Solution:
    '''Дано целое число n.
    Нужно вернуть все числа от 1 до n включительно, отсортированные в лексикографическом (словесном) порядке.

    Твоя задача — написать эффективный алгоритм, который работает:

    за O(n) по времени
    и использует O(1) дополнительной памяти (кроме результата)
    📘 Что значит "лексикографически"?
    Это порядок, в котором слова идут в словаре. Числа сравниваются как строки:

    "1" < "10" < "11" < "2" < "3" и так далее.
    ✅ Примеры:
    🔹 Пример 1:

    Вход:
    n = 13

    Выход:
    [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]

    Пояснение:
    Числа от 1 до 13:
    [1, 2, 3, ..., 13]
    Если отсортировать их как строки:
    ["1", "10", "11", "12", "13", "2", ..., "9"]
    '''
    def lexicalOrder(self, n: int) -> list[int]:


        def merge_sort(lst):
            if len(lst) <= 1:
                return lst

            middle = len(lst) // 2
            left, right = merge_sort(lst[:middle]),  merge_sort(lst[middle:])
            return merge(left, right)

        def merge(left, right):
            result = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            result.extend(left[i:]), result.extend(right[j:])
            return result

        def result_function():

            return list(map(int, merge_sort(list(map(str, range(1, n + 1))))))
        return result_function()





sol = Solution()
print(sol.lexicalOrder(13))