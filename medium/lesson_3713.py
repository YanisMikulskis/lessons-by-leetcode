from collections import Counter
class Solution:
    '''
    Средняя сложность
    Дана строка s, состоящая из строчных букв английского алфавита.
    Подстрока строки s называется сбалансированной, если все различные символы в этой подстроке встречаются одинаковое количество раз.
    Необходимо вернуть длину самой длинной сбалансированной подстроки строки s.
    🔎 Пояснение к определению
    Подстрока — это непрерывная последовательность символов строки.
    Сбалансированная подстрока означает:
    Если в подстроке 1 уникальный символ → он может встречаться любое количество раз (это всегда сбалансировано).
    Если 2 уникальных символа → каждый должен встречаться одинаковое число раз.
    Если 3 уникальных символа → все три должны встречаться одинаковое число раз.
    И так далее.
    Формально:
    Если множество уникальных символов имеет размер k, и каждый из них встречается f раз, то длина подстроки равна k × f.
    🧠 Примеры
    ✅ Пример 1
    s = "aabb"
    Разберём подстроки:
    "aa" → только a, встречается 2 раза → сбалансировано
    "bb" → только b, встречается 2 раза → сбалансировано
    "aabb" → a = 2, b = 2 → сбалансировано ✅
    Максимальная длина = 4
    Ответ: 4
    '''
    def longestBalanced(self, s: str):
        def check_substring(sub:str) -> bool:
            ans = 0
            for let, cnt in Counter(sub).items():
                if not ans:
                    ans = cnt
                else:
                    if cnt != ans:
                        return False
            return True

        def call_func_check(ans, i, j):
            if check_substring(sub=sub):
                length = j - i
                ans = length if length > ans else ans
            return ans

        i,j,ans_1 = 0, len(s),0
        while i < len(s) - 1:
            if i == j:
                i, j = i + 1, len(s)
            sub = s[i:j]
            ans_1 = call_func_check(ans=ans_1, i=i, j=j)
            j -= 1

        i,j,ans_2 = 0, len(s), 0
        while j > 0:
            if i == j:
                i, j = 0, j - 1
            sub = s[i:j]
            ans_2 = call_func_check(ans=ans_2, i=i, j=j)
            i += 1

        return max(ans_1, ans_2)

sol = Solution()
# print(sol.longestBalanced("zzabccy"))
a = '11'
b = '1'


ans = 0
def func(number):
    ans = 0
    for i in range(len(number)):
        if number[len(number) - 1 - i] != '0':
            ans += 2 ** i
    return ans
print(func(a) + func(b))



