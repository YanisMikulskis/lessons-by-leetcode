from collections import Counter
class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()
        min_el, result = float('inf'), []
        for i in range(len(arr) - 1):
            couple = abs(arr[i] - arr[i + 1])
            if couple < min_el:
                result, min_el = [], couple
                result.append([arr[i], arr[i + 1]])
            elif couple == min_el:
                result.append([arr[i], arr[i + 1]])


        return result

sol = Solution()
print(sol.minimumAbsDifference(arr = [3, 8, -10, 23, 19, -4, -14, 27]))