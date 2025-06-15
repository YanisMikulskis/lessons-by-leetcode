from collections import Counter
class Solution:
    '''
    Дан массив целых чисел nums и положительное число k.
    Нужно посчитать количество подмассивов, в которых максимальный элемент массива встречается хотя бы k раз.

    📌 Подмассив — это непрерывная последовательность элементов исходного массива.

    📥 Ввод:
    nums: список целых чисел, например [1, 3, 2, 3, 3]
    k: целое положительное число, например 2
    📤 Вывод:
    Целое число — количество подходящих подмассивов
    📌 Пример 1:

    Вход: nums = [1, 3, 2, 3, 3], k = 2
    Выход: 6
    📊 Объяснение:

    Максимальный элемент в массиве — это 3. Подмассивы, где элемент 3 встречается ≥ 2 раз:

    [1, 3, 2, 3]
    [1, 3, 2, 3, 3]
    [3, 2, 3]
    [3, 2, 3, 3]
    [2, 3, 3]
    [3, 3]
    Итого: 6 подмассивов ✅
    '''
    def countSubarrays(self, nums: list[int], k: int) -> int:
        n, max_element, res = len(nums), max(nums), 0
        for i in range(n):
            step = i + k
            if len(nums[i:step]) < k:
                break
            step = n if step > n else step
            counter_max = Counter(nums[i:step])[max_element]
            while counter_max < k and step < n:
                if nums[step] == max_element:
                    counter_max += 1
                step += 1
            if counter_max >= k:
                res += (1 + n - step)
        return res



        #
        # res = 6
        # res = 0
        # res = 8
        # res = 6
        # res = 5
        # res = 0





            #     if nums[step] == max_element:
            #         counter_max += 1
            #     step += 1
            # else:
            #     res += 1
            #     print(f'rr = {n - 1 - step}')











            #
            # if counter[max_element] >= k:
            #     res += 1
            #     res += n - 1 - i
            #
            # print(counter)



sol = Solution()
sol.countSubarrays(nums = [1, 3, 2, 3, 3], k = 2)
sol.countSubarrays(nums = [1,4,2,1], k = 3)
sol.countSubarrays(nums = [5, 1, 5, 2, 5, 3], k = 2)
sol.countSubarrays(nums = [7, 7, 7, 7, 7], k = 3)
sol.countSubarrays(nums = [4, 3, 4, 2, 4, 1, 4], k = 3
)
sol.countSubarrays(nums = [6, 1, 2, 3, 4], k = 2)
arr = [1,2,3]
coun = Counter(arr
               )
coun[4] += 1
print(coun)