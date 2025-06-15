# class Solution:
#     '''
#     Условие задачи:
#
#     Дан массив целых чисел arr, и три целых числа a, b и c.
#
#     Тебе нужно найти количество хороших триплетов в массиве.
#
#     Триплет (arr[i], arr[j], arr[k]) считается хорошим, если выполняются следующие условия:
#
#     0 <= i < j < k < arr.length
#     |arr[i] - arr[j]| <= a
#     |arr[j] - arr[k]| <= b
#     |arr[i] - arr[k]| <= c
#     Где |x| — это абсолютное значение числа x (модуль).
#     '''
#     def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
#
#
#         i,j,k = 0, 1, 2
#         res = 0
#         while i <= len(arr) - 3:
#             i_el, j_el, k_el = arr[i], arr[j], arr[k]
#             if abs(i_el - j_el) <= a:
#                 if abs(j_el - k_el) <= b:
#                     if abs(i_el - k_el) <= c:
#                         res += 1
#             k += 1
#             if k == len(arr):
#                 j += 1
#                 if j == len(arr) - 1:
#                     i += 1
#                     j = i + 1
#                 k = j + 1
#         return res









# sol = Solution()
# sol.countGoodTriplets(arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3)
# # sol.countGoodTriplets(arr = [1,1,2,2,3], a = 0, b = 0, c = 1)
















# Input: nums1 = [4,0,1,3,2], nums2 = [4,1,0,2,3]
# Output: 4
# Explanation: The 4 good triplets are (4,0,3), (4,0,2), (4,1,3), and (4,1,2).


class Solution:
    def goodTriplets(self, nums1: list[int], nums2: list[int]) -> int:
        step, idx = 1, 0
        dp1, dp2 = [], []
        sets = set()
        while idx < len(nums1) - 2:
            dp1.append(f'{nums1[idx]}{nums1[step]}')
            dp2.append(f'{nums2[idx]}{nums2[step]}')
            others = set(dp1) & set(dp2)
            if others:
                sets.update(others)

            step += 1
            if step == len(nums1) - 1:
                idx += 1
                step = idx + 1

        set_1, set_2 = set(), set()

        def add_sets(couple, lst, set_param, pos = None):
            for j in range(len(lst)):
                if lst[j] == int(couple[1]):
                    pos = j
                if pos is not None and j > pos:
                    set_param.add(f'{couple}{lst[j]}')

        for couple in sets:
            add_sets(couple, nums1, set_1)
            add_sets(couple, nums2, set_2)
        return len(set_1 & set_2)



sol = Solution()
# sol.goodTriplets(nums1 = [4,0,1,3,2], nums2 = [4,1,0,2,3])
# # print(f'-------')
# sol.goodTriplets(nums1 = [2,0,1,3], nums2 = [0,1,2,3])
sol.goodTriplets(nums1 = [0, 1, 2, 3, 4],
nums2 = [1, 0, 2, 4, 3])
arr = list(enumerate([10,11,12]))
print(arr)
