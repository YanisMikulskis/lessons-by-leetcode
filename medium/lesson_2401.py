from itertools import combinations
class Solution:
    '''
    Перевод задачи:
    Дан массив nums, состоящий из положительных целых чисел.
    Мы называем подмассив хорошим (nice), если побитовая операция AND для каждой пары элементов,
    находящихся в разных позициях в этом подмассиве, равна 0.
    Необходимо вернуть длину самого длинного хорошего подмассива.
    Подмассив — это непрерывная часть массива.

    Заметьте, что подмассивы длины 1 всегда считаются хорошими.
    Примеры:
    Пример 1:

    Вход:
    nums = [1, 3, 8, 48, 10]

    Выход:
    3

    Объяснение:
    Подмассив [1, 3, 8] является хорошим, так как:
    1 & 3 = 1
    1 & 8 = 0
    3 & 8 = 0
    (Одна из пар дает ненулевой результат, значит [1, 3, 8] не подходит)
    Подмассив [8, 48, 10] является хорошим, так как:
    8 & 48 = 0
    8 & 10 = 0
    48 & 10 = 0
    (Все AND-операции дают 0, значит подмассив подходит)
    Максимальная длина хорошего подмассива — 3 ([8, 48, 10]).

    '''

    def longestNiceSubarray(self, nums: list[int]) -> int:
        point_1 = 0
        point_2 = 1
        self.bits = {

        }
        def bit_couple(minilst):

            if len(minilst) == 1:

                return True
            self.bits.setdefault(tuple(minilst), [])
            def func(idx1, idx2):

                if idx1 == len(minilst) - 1: # если побитовое И во всех парах равно нулю

                    return True

                if minilst[idx1] & minilst[idx2] != 0:
                    self.bits[tuple(minilst)].append(minilst[idx1] & minilst[idx2])
                    return False

                self.bits[tuple(minilst)].append(minilst[idx1] & minilst[idx2])
                print(self.bits)

                if idx2 == len(minilst) - 1:
                    idx2 = idx1 = idx1 + 1

                return func(idx1, idx2 + 1)
            return func(0, 1)



        len_slice = 0
        while point_1 < len(nums) - 1:
            if point_2 == len(nums):
                point_1 += 1
                point_2 = point_1 + 1
            slice = nums[point_1:point_2]
            print(slice)
            if bit_couple(slice):
                if len(slice) > len_slice:
                    len_slice = len(slice)
            point_2 += 1
        return len_slice

sol = Solution()
# sol.longestNiceSubarray([1,3,8,48,10])
# sol.longestNiceSubarray([3, 1, 5, 11, 13])
# sol.longestNiceSubarray([2, 3, 4, 5])
# print(sol.longestNiceSubarray([135745088,609245787,16,2048,2097152]))
# print(sol.longestNiceSubarray([1,3,8,48,10]))
# print(sol.longestNiceSubarray([3,1,5,11,13]))
print(sol.longestNiceSubarray([135745088,609245787,16,2048,2097152]))

# def func(result, idx1, idx2):
#     if idx1 == len(arr) - 1:
#         return result
#     result.append([arr[idx1], arr[idx2]])
#     if idx2 == len(arr) - 1:
#         idx2 = idx1 = idx1 + 1
#     return func(result, idx1, idx2 + 1)
#
# print(func([], 0, 1))
from itertools import combinations

# print(list(combinations(arr, 2)))


class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        max_length = 1  # Track the maximum nice subarray length found

        for start in range(len(nums) - max_length):
            current_length = 1  # Length of current nice subarray
            used_bits = nums[start]  # Track which bits are used in our subarray

            # Try to extend the subarray
            for end in range(start + 1, len(nums)):
                # If no bits overlap between current number and used bits, we can extend
                if (used_bits & nums[end]) == 0:
                    used_bits |= nums[
                        end
                    ]  # Add new number's bits to our tracker
                    current_length += 1
                # If bits overlap, this number can't be part of our nice subarray
                else:
                    break

            # Update max length if we found a longer nice subarray
            max_length = max(max_length, current_length)

        return max_length