class Solution:
    '''
    Вам дан массив целых чисел nums, индексируемый с 0.

    Верните максимальное значение среди всех троек индексов (i, j, k) таких, что i < j < k. Если все такие тройки имеют отрицательное значение, верните 0.

    Значение тройки индексов (i, j, k) вычисляется как (nums[i] - nums[j]) * nums[k].

    Примеры:

    Пример 1:

    Вход: nums = [12, 6, 1, 2, 7]
    Объяснение:
    Рассмотрим все возможные тройки (i, j, k) с i < j < k:

    (0, 1, 2): значение = (12 - 6) * 1 = 6
    (0, 1, 3): значение = (12 - 6) * 2 = 12
    (0, 1, 4): значение = (12 - 6) * 7 = 42
    (0, 2, 3): значение = (12 - 1) * 2 = 22
    (0, 2, 4): значение = (12 - 1) * 7 = 77
    (0, 3, 4): значение = (12 - 2) * 7 = 70
    (1, 2, 3): значение = (6 - 1) * 2 = 10
    (1, 2, 4): значение = (6 - 1) * 7 = 35
    (1, 3, 4): значение = (6 - 2) * 7 = 28
    (2, 3, 4): значение = (1 - 2) * 7 = -7
    Максимальное значение среди всех троек — 77.
    Ответ: 77
    '''
    def maximumTripletValue(self, nums: list[int]) -> int:
        dict_prog = {
        }
        key = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) - 1):
                dict_prog[key] = [[nums[i], nums[j]], j + 1]
                key += 1

        temp, result =0, []

        for k,v in dict_prog.items():
            for j in range(v[1], len(nums)):
                sub = v[0][0] - v[0][1]
                if sub < 0:
                    continue
                calc = sub * nums[j]
                if calc > temp:
                    temp, result = calc, [*v[0], nums[j]]

        return temp if result else 0
        # for k,v in dict_prog.items():




sol = Solution()
# print(sol.maximumTripletValue([12, 6, 1, 2, 7])) #может сначала сделать все вычитания а потом результаты постепенно умножить?
# # print(sol.maximumTripletValue([1,10,3,4,19]))
# print(sol.maximumTripletValue([5, 4, 3, 2, 1]))
# print(sol.maximumTripletValue(nums = [10, 5, 8, 3, 2]))

print(sol.maximumTripletValue([1,2,3]))