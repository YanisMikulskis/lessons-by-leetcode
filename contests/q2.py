class Solution:
    '''
    Перевод задачи:
    Вам дан круглый массив nums и массив запросов queries.

    Для каждого запроса i вам нужно найти следующее:

    Минимальное расстояние между элементом на индексе queries[i] и любым другим индексом
    j в круглом массиве, где nums[j] == nums[queries[i]]. Если такого индекса не существует,
    ответ для этого запроса должен быть -1.
    Возвращайте массив answer, который будет иметь тот же размер, что и queries, где answer[i]
     представляет результат для запроса i.

    Примеры:
    Пример 1:

    Ввод:

    nums = [3, 1, 2, 4, 2, 1]
    queries = [0, 4, 3]
    Объяснение:

    Для запроса queries[0] = 0: nums[0] = 3. Нужно найти минимальное расстояние между элементом 3
    и другими индексами, где встречается 3. В данном случае только индекс 0 содержит 3, следовательно,
     ответ будет -1, так как нет другого индекса с таким значением.
    Для запроса queries[1] = 4: nums[4] = 2. Элемент 2 встречается на индексах 2 и 4. Минимальное
     расстояние между этими индексами (с учётом круговой структуры массива) равно 2. Ответ для этого запроса будет 2.
    Для запроса queries[2] = 3: nums[3] = 4. В массиве нет других индексов с элементом 4. Ответ будет -1.
    Вывод:

    [-1, 2, -1]
    '''
    def solveQueries(self, nums: list[int], queries: list[int]) -> list[int]:






        def function(idx):  # 3 2 4 elements
            temp = nums[idx]
            if nums.count(temp) == 1:
                return -1
            circular = nums[:idx] + nums[idx:] + nums[:idx]

            step_left, step_right = 1, 1
            dist = []


            for i in range(idx - 1, -1, -1):
                if circular[i] == temp:
                    dist.append(step_left)
                    break
                step_left += 1

            for i in range(idx + 1, len(circular)):
                if circular[i] == temp:
                    dist.append(step_right)
                    break
                step_right += 1
            return min(dist)





        # def function(idx):  # 3 2 4 elements
        #     temp = nums[idx]
        #     if nums.count(temp) == 1:
        #         return -1
        #     step_right = idx + 1 if idx < len(nums) - 1 else 0
        #     dist_right = 1
        #     distance = []
        #     while nums[step_right] != temp: #->
        #         step_right += 1
        #         if step_right == len(nums):
        #             step_right = 0
        #         dist_right += 1
        #     else:
        #         distance.append(dist_right)
        #
        #     step_left = idx - 1
        #     dist_left = 1
        #     while nums[step_left] != temp:
        #         step_left -= 1
        #         if step_left == -1:
        #             step_left = len(nums) - 1
        #         dist_left += 1
        #     else:
        #         distance.append(dist_left)
        #     print(f'fdfd {distance}')
        #     return min(distance)








        return [function(i) for i in queries]



sol = Solution()
print(sol.solveQueries(nums = [3, 1, 2, 4, 2, 1], queries = [0, 4, 3])) # => [-1, 2, -1] [3, 1, 2, 4, 2, 1, 3, 1, 2, 4]

print(sol.solveQueries(nums = [5, 4, 5, 2, 5, 3], queries = [0, 4, 1, 2]))


print(sol.solveQueries([1,3,1,4,1,3,2], [0,3,5]))


print(sol.solveQueries([1,2,3,4], [0,1,2,3]))



print(sol.solveQueries([2,10,20,20,20], [1,4,2]))