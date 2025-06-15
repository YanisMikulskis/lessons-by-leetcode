
class Solution:
    '''
    Дано целое число n.

    Каждое число от 1 до n включительно группируется по сумме своих цифр.

    Нужно вернуть количество таких групп, которые имеют наибольший размер
    (то есть максимальное количество элементов).
    Пример 1:

    Ввод: n = 13
    Группы:
    Сумма 1: [1, 10]
    Сумма 2: [2, 11]
    Сумма 3: [3, 12]
    Сумма 4: [4, 13]
    Сумма 5: [5]
    Сумма 6: [6]
    Сумма 7: [7]
    Сумма 8: [8]
    Сумма 9: [9]

    Самые большие группы по размеру (размер 2): [1,10], [2,11], [3,12], [4,13]

    ➡️ Ответ: **4**
    '''
    def countLargestGroup(self, n: int) -> int:
        test = {

        }
        for number in range(1, n + 1):
            sum_number = sum(list(map(int, str(number))))
            if sum_number not in test:
                test.setdefault(sum_number, 0)
            test[sum_number] += 1
        return len([val for val in test.values() if val == max(test.values())])











sol = Solution()

print(sol.countLargestGroup(13))
print(f'----')
# sol.countLargestGroup(14)
# print(f'----')
# sol.countLargestGroup(15)
# print(f'----')
# sol.countLargestGroup(16)
# print(f'----')
# sol.countLargestGroup(5)
# sol.countLargestGroup(9000)
#
# for i in range(100, 10000, 100):
#     sol.countLargestGroup(i)
#     print(f'------')
# sol.countLargestGroup(2)
# sol.countLargestGroup(24)