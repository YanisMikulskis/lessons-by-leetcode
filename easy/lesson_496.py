class Solution:
    '''
    📘 Перевод задачи
    496. Следующий больший элемент I
    Следующий больший элемент для числа x в массиве — это первый элемент справа от x, который строго больше x.
    Даны два массива целых чисел с уникальными элементами (без повторов):
    nums1
    nums2
    При этом nums1 является подмножеством nums2.
    Для каждого элемента nums1[i]:
    Найдите индекс j, такой что nums1[i] == nums2[j]
    Определите следующий больший элемент для nums2[j] в массиве nums2
    Если такого элемента нет — ответ -1
    Нужно вернуть массив ans, где:
    ans[i] — следующий больший элемент для nums1[i]
    🧠 Простое объяснение
    Мы смотрим на элемент из nums1
    Ищем его в nums2
    Двигаемся вправо и ищем первое число, которое больше
    Если нашли — записываем его
    Если нет — -1
    📊 Пример 1 (из условия)
    Вход:
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    Разбор:
    🔹 Элемент 4
    nums2 = [1, 3, 4, 2]
             ↑
    Справа от 4 нет числа больше → -1
    🔹 Элемент 1
    nums2 = [1, 3, 4, 2]
        ↑
    Первое большее справа — 3 → 3
    🔹 Элемент 2
    nums2 = [1, 3, 4, 2]
              ↑
    Справа ничего нет → -1
    Выход:
    [-1, 3, -1]

    '''
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                for j in range(len(nums2)):
                    if nums2[j] == nums1[i]:
                        for k in range(j, len(nums2)):
                            if nums2[k] > nums2[j]:
                                result.append(nums2[k])
                                break
                        else:
                            result.append(-1)
                            break
        print(result)

        stack = []
        great = {

        }
        for num in nums2:
            while stack and num > stack[-1]:
                great[stack.pop()] = num
            stack.append(num)
        else:
            for num in stack:
                great[num] = -1
        return [great[num] for num in nums1]



sol = Solution()
print(sol.nextGreaterElement(nums1=[1,3,5,2,4], nums2=[6,5,4,3,2,1,7]))