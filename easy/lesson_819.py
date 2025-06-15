from collections import Counter
from string import punctuation
import re
class Solution:
    '''
    Задача: Наиболее частое слово (Most Common Word)
    Уровень сложности: Лёгкий

    Условие:

    Дан текст paragraph (строка) и массив строк banned, содержащий запрещённые слова.
    Нужно вернуть слово, которое встречается чаще всего в тексте и не входит в список запрещённых.
    Гарантируется, что такое слово существует и оно единственное.

    Слова в тексте не чувствительны к регистру, а ответ нужно вернуть в нижнем регистре.

    Знаки препинания не считаются частью слов.

    Примеры:
    Пример 1:

    Ввод:

    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    Вывод:

    "ball"
    Пояснение:

    Слово "hit" встречается 3 раза, но оно запрещено.
    Слово "ball" встречается 2 раза и не запрещено.
    Все остальные слова встречаются только 1 раз.
    Следовательно, "ball" — самое частое допустимое слово.
    '''
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        new_paragraph = re.split(r'[^a-zA-Z]+', paragraph)
        new_paragraph = [word.lower() for word in new_paragraph if word and word.lower() not in banned]
        return max(Counter(new_paragraph).items(), key=lambda x: x[1])[0]






sol = Solution()
# print(sol.mostCommonWord(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]))
# print(sol.mostCommonWord(paragraph = "a.", banned = []))
# print(sol.mostCommonWord("a, a, a, a, b,b,b,c, c", ['a']))
# print(sol.mostCommonWord("Bob", []))
# print(sol.mostCommonWord("..Bob hit a ball, the hit BALL flew far after it was hit.", ['hit']))

# str = 'qwerty'
#
# num = 3
# ret = []
# for i in range(len(str) - 1):
#     ret.append(str[:i])
#     ret.append(str[i:i + 1])
#     ret.append(str[i + 1:])
# print(ret)
#
#
# left,right = 0, 1
# res = []
# while right < len(str):
#     res.append(str[:right])
#     res.append(str[right:])
#     right += 1
# print(res)













