class Solution:
    '''
    Условие задачи (перевод):
    Тебе даны два целых числа:

    n — длина массива
    maxValue — максимальное допустимое значение элементов
    Массив arr длины n называется идеальным, если:

    Каждый элемент массива arr[i] принадлежит диапазону от 1 до maxValue
    Для каждого i от 1 до n - 1:
    arr[i] % arr[i - 1] == 0,
    то есть, каждый следующий элемент делится на предыдущий
    Найди количество различных идеальных массивов длины n.
    Верни ответ по модулю 10⁹ + 7.

    📌 Примеры:
    Пример 1:

    n = 2
    maxValue = 5
    ✅ Возможные массивы:

    [1,1], [1,2], [1,3], [1,4], [1,5],
    [2,2], [2,4],
    [3,3],
    [4,4],
    [5,5]
    Их 10 штук → ответ: 10
    '''
    def idealArrays(self, n: int, maxValue: int) -> int:

        res = 0
        dp = [[1] * (n - 1) + [num] for num in range(1, maxValue + 1)]

        temps = []
        for i in range(1, len(dp)):
            temp = [dp[i]]
            for j in range(len(dp[i]) - 2, -1, -1):
                dp_copy = temp[-1].copy()
                dp_copy[j] = dp_copy[j + 1]
                temp.append(dp_copy)
            print(f'temp = {temp}')
            temps += temp
            # print(f'temp = {temp}')
            # temps.append(*temp)
        print(f'temps {temps}')
        # res += len(dp) + ((n - 1) * (len(dp)-1))
        res += maxValue + ((n - 1) * (maxValue - 1))
        print(res)
        #
        #
        var = 5
        rem = []
        test = [1,1,1]
        def func(test, rem, idx):
            test_copy = test.copy()
            new_el = test_copy[-idx] + 1
            if new_el % test_copy[-idx-1] == 0:
                t
            test_copy[idx]

        func([1,1,1], [], 1)

sol = Solution()
sol.idealArrays(3, 5)
# (1 + ) * (n - 1)
# sol.idealArrays(4, 5)
# # sol.idealArrays(3, 5)
# sol.idealArrays(2, 5)
# print()
# sol.idealArrays(4, 6)
# sol.idealArrays(3, 6)
# sol.idealArrays(2, 6)
# print()
# sol.idealArrays(4, 8)
# sol.idealArrays(3, 8)
# sol.idealArrays(2, 8)

1 1 1
1 1 2       1 2 2      1 4 4
1 1 4       1 2 4


i = 1

for j in range(2, 5):
    i += j

print(f'i = {i}')