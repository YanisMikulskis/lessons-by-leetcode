# from string import ascii_lowercase as alp
# class Solution:
#     '''
#     Уровень сложности: Средний
#     Темы: Строки, Списки, Графы, Объединение множеств (Union-Find)
#
#     📜 Условие (перевод):
#     Тебе даны:
#
#     две строки одинаковой длины: s1 и s2,
#     строка baseStr.
#     Каждая пара символов на одинаковых позициях в s1 и s2 считается эквивалентной.
#
#     ✅ Эквивалентность означает:
#
#     Если:
#
#     s1 = "abc"
#     s2 = "cde"
#     То эквивалентны:
#
#     'a' == 'c'
#     'b' == 'd'
#     'c' == 'e'
#     Эквивалентность работает по правилам отношений эквивалентности:
#
#     Рефлексивность: 'a' == 'a'
#     Симметричность: если 'a' == 'b', то 'b' == 'a'
#     Транзитивность: если 'a' == 'b' и 'b' == 'c', то 'a' == 'c'
#     🎯 Задача:
#     Используя информацию об эквивалентных символах из s1 и s2, преврати строку baseStr в лексикографически наименьшую эквивалентную строку.
#
#     То есть, для каждого символа в baseStr — замени его на наименьший (по алфавиту) символ из его эквивалентного множества.
#     ✅ Примеры:
#     Пример 1:
#
#     Ввод:
#     s1 = "abc"
#     s2 = "cde"
#     baseStr = "eed"
#
#     Пояснение:
#     Символы эквивалентны:
#     'a' == 'c' == 'e'
#     'b' == 'd'
#
#     → Тогда "eed" можно заменить на:
#     - 'e' → 'a'
#     - 'e' → 'a'
#     - 'd' → 'b'
#
#     Результат:
#     "aab"
#     '''
#     def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # zip_list = list(zip(s1, s2))
        # graph = {
        #
        # }
        # for couple in zip_list:
        #     if couple[0] not in graph:
        #         graph.setdefault(couple[0], [])
        #     if couple[1] not in graph[couple[0]]:
        #         graph[couple[0]].append(couple[1])
        #
        #     if couple[1] not in graph:
        #         graph.setdefault(couple[1], [])
        #     if couple[0] not in graph[couple[1]]:
        #         graph[couple[1]].append(couple[0])
        #
        #
        # for k in graph:
        #     new_neight = set(graph[k])
        #     for val in graph[k]:
        #         new_neight.update(graph.get(val, []))
        #     new_neight.discard(k)
        #     graph[k] = list(new_neight)
        #
        #
        #
        #
        #
        # res = ''
        # for k in baseStr:
        #     try:
        #
        #         res += min([k, *graph[k]])
        #         # print(f'k = {k}  {graph[k]}')
        #     except KeyError:
        #
        #         res += k
        # return res








        #
        # for core, branch in graph.items():
        #     if branch in graph:





# sol = Solution()
# # sol.smallestEquivalentString(s1 = "abc", s2 = "cde", baseStr = "eed")
# print(sol.smallestEquivalentString("cgokcgerolkgksgbhgmaaealacnsshofjinidiigbjerdnkolc",
#                              "rjjlkbmnprkslilqmbnlasardrossiogrcboomrbcmgmglsrsj",
#                              "bxbwjlbdazfejdsaacsjgrlxqhiddwaeguxhqoupicyzfeupcn"))




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