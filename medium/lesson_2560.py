class Solution:
    '''
    Условие
    Вам дана неотсортированная целочисленная последовательность nums длины n и целое число k (1 ≤ k ≤ n).

    Вам нужно выбрать подмножество из k домов (чисел) таким образом, чтобы максимальное число среди выбранных элементов было минимально возможным.

    Верните минимально возможное значение максимального числа в выбранном подмножестве.
    Примеры

    Пример 1
    Вход:

    nums = [1, 3, 2, 3, 5, 1, 3, 7, 9]
    k = 3
    Выход:

    3
    Объяснение:

    Нам нужно выбрать k = 3 числа.
    Возможные выборы:
    {1, 3, 2} → max = 3
    {1, 3, 3} → max = 3
    {2, 3, 3} → max = 3
    {1, 3, 1} → max = 3
    {3, 3, 3} → max = 3
    {1, 3, 5} → max = 5 (хуже, чем 3)
    Минимальное возможное максимальное число = 3.
    '''
    def minCapability(self, nums: list[int], k: int) -> int:
        minimals = []

        while k > 0:
            min_middle = min(nums)
            indexes = nums.index(min_middle)
            minimals.append(min_middle)
            nums[indexes] = None
            if len(nums) - 1 > indexes > 0:
                nums[indexes - 1], nums[indexes + 1] = None, None
            elif indexes == len(nums) - 1:
                nums[indexes - 1] = None
            else:
                nums[indexes + 1] = None
            nums = [i for i in nums if i is not None]
            k -= 1
        return max(minimals)


        # while
        # left = nums[:indexes - 1] #соседей сразу исключаем
        # right = nums[indexes + 2:]
        # minimals = [nums[indexes]]
        # nums[indexes]
        # while k > 0:
        #     min_left =  min(left)


sol = Solution()
print(sol.minCapability(nums = [5, 3, 2, 9, 10], k = 2))
print(sol.minCapability(nums = [10, 100, 200, 300, 400], k = 3))
print(sol.minCapability(nums = [2,7,9,3,1], k = 2))
print(sol.minCapability(nums = [1, 3, 2, 3, 5, 1, 3, 7, 9], k = 3))
print(sol.minCapability([9,6,20,21,8], 3))
