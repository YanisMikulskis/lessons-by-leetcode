class Solution:
    '''
    Перевод задачи: Решение вопросов с помощью мозговой силы
    Уровень сложности: Средний

    Условие

    Дан 0-индексированный двумерный массив целых чисел questions, где:

    questions[i] = [pointsi, brainpoweri]
    Этот массив описывает вопросы экзамена, где каждый вопрос можно либо решить, либо пропустить.

    Правила:

    Вопросы рассматриваются по порядку (начиная с вопроса 0).
    Если решается вопрос i:
    Получаете pointsi очков.
    Пропускаете следующие brainpoweri вопросов.
    Если вопрос i пропускается, переходите к следующему вопросу.
    Примеры

    📌 Пример 1
    Вход:

    questions = [[3,2], [4,3], [4,4], [2,5]]
    Рассмотрение вариантов:

    Если решить 0-й вопрос (3 очка), то пропустим вопросы 1 и 2, можем взять только 3-й (итог: 3 + 2 = 5).
    Если пропустить 0-й и решить 1-й (4 очка), то пропустим вопросы 2 и 3 (итог: 4).
    Если пропустить 0-й и 1-й, но взять 2-й (4 очка), затем уже ничего нельзя взять (итог: 4).
    Оптимальный вариант — взять 0-й и 3-й: 5 очков.
    Выход:

    5
    '''
    def mostPoints(self, questions: list[list[int]]) -> int:

        def function(idx, lst, score):
            if idx >= len(lst):
                return score
            if score != 0:
                inc = lst[idx][0]
                if idx < len(lst) - 1:
                    max_lst = max(lst[idx + 1:], key=lambda x:x)[0]
                else:
                    max_lst = inc
                if max_lst > inc:
                    score += max_lst
                else:
                    score += inc
            else:
                score += lst[idx][0]
            return function(idx + lst[idx][1] + 1, lst, score)

        results = [0]
        for i in range(len(questions)):
            score = function(i, questions, 0)
            if score > results[0]:
                results[0] = score

        print(results[0])
        return results[0]

# sol = Solution()
# sol.mostPoints(questions = [[3,2], [4,3], [4,4], [2,5]])
# # sol.mostPoints([[10, 1], [20, 1], [30, 1], [40, 1], [50, 1]])
# sol.mostPoints([[21,5],[92,3],[74,2],[39,4],[58,2],[5,5],[49,4],[65,3]])
# arr = []
# arr += 1
# print(arr)

nums = [1,2,3]
subsets = [[]]

#[[1],[1,2],[1,3],[1,4],[1,2,3],[1,3,4],[1,2,3,4],[2],[2,3],[2,4],[2,3,4],[3],[3,4],[4]

# def req(left, right, lst, subs):
#     if left == len(lst) - 1:
#         return subs
#     subs.append([lst[left], lst[right]])
#     if right == len(lst) - 1:
#         right = left = left + 1
#     return req(left, right + 1, lst, subs)
#
# def req(left, right, lst, sub):
#     if left == len(lst) - 1:
#         return sub
#     if right == len(lst):
#         right = left = left + 1
#
#     sub.append(lst[left:right + 1])
#
#     return req(left, right + 1, lst, sub)
#
# print(req(0,0 ,arr, [[]]))


# def req(left, right, lst, sub):
#     if left == len(lst):
#         return sub
#     sub.append(lst[l])
#     if right == len(locals())
#
#
# # Проверка
# arr = [1, 2, 3, 4]
# print(req(0, 0, arr, [[]]))
# print(req(0, 1, arr, [[]]))
# for i in range(len(arr)):
#     subsets.append([arr[i]])
#     for j in range(i + 1, len(arr)):
nums = [12, 6, 1, 2, 7]

triples = [0]

def req(start, path):

    if len(path) == 3:
        res = (path[0] - path[1]) * path[2]
        if res > 0 and res > triples[0]:
            triples[0] = res

    for i in range(start, len(nums)):
        path.append(nums[i])
        req(i + 1, path)
        path.pop()

print(req(0, []))
print(triples)
