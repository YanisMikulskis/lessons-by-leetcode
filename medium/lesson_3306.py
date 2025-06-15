class Solution:
    '''
    Условие задачи: Вам дана строка word и неотрицательное целое число k. Необходимо вернуть общее
    количество подстрок строки word, которые содержат каждую из гласных ('a', 'e', 'i', 'o' и 'u')
    хотя бы один раз и ровно k согласных.

    Примеры:

    Входные данные:
    word = "aeioqq"
    k = 1
    Выходные данные: 0
    Объяснение: Нет подстроки, содержащей все гласные.

    Входные данные:
    word = "aeiou"
    k = 0
    Выходные данные: 1
    Объяснение: Единственная подстрока, содержащая все гласные и ноль согласных, — это "aeiou".

    Входные данные:
    word = "ieaouqqieaouqq"
    k = 1
    Выходные данные:3

    Объяснение: Подстроки, содержащие все гласные и одну согласную:
    word[0..5] = "ieaouq"
    word[6..11] = "qieaou"
    word[7..12] = "ieaouq"
    Для решения этой задачи необходимо перебрать все возможные подстроки строки word и проверить,
    содержат ли они все гласные хотя бы один раз и ровно k согласных. Это можно сделать с помощью двух
    вложенных циклов, которые будут определять начало и конец подстроки, и дополнительной проверки
    для подсчёта гласных и согласных в текущей подстроке.

    Обратите внимание, что при больших размерах строки такой подход может быть неэффективным,
    поэтому стоит подумать об оптимизациях, например, используя скользящее окно или другие методы
    для уменьшения количества проверок.
    '''
    def countOfSubstrings(self, word: str, k: int) -> int:
        all_strings = []
        test_string = '1234'
        iteration = sum(range(1, len(word)))
        vowels_let = {'a', 'e', 'i', 'o' , 'u'}
        start, end, min_length = 0, 1, len(vowels_let)


        for i in range(iteration):
            if end > len(word):
                start += 1
                end = start + 1

            mini_word = word[start:end]

            if len(mini_word) > 5:
                check_vowels = set([let for let in mini_word if let in vowels_let])
                if check_vowels == vowels_let:
                    count_consonants = k
                    for i in mini_word:

                        if not count_consonants:
                            break

                        if i not in check_vowels:

                            all_strings.append(mini_word)
                            count_consonants -= 1
                            break



            # all_strings.append(word[start:end])
            end += 1
        print(all_strings)


sol = Solution()
sol.countOfSubstrings("ieaouqqieaouqq", 1)