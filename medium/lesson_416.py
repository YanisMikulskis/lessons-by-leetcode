from itertools import permutations
class Solution:
    def canPartition(self, nums: list[int]) -> bool:

        # def fact(n):
        #     if n == 1:
        #         return n
        #     return n * fact(n - 1)
        dp = []

        def permute(nums):
            def backtrack(start):
                if start == len(nums):
                    result.append(nums.copy())  # Копируем текущую перестановку
                    return
                for i in range(start, len(nums)):
                    print(nums)
                    nums[start], nums[i] = nums[i], nums[start]  # Меняем местами

                    backtrack(start + 1)  # Рекурсивный вызов
                    nums[start], nums[i] = nums[i], nums[start]  # Возвращаем назад (backtrack)

            result = []
            backtrack(0)
            return result

        # Пример использования
        nums = [1, 2, 3]
        print(permute(nums))

        print(list(permutations(nums)))
sol = Solution()
sol.canPartition([1,2,3,4])