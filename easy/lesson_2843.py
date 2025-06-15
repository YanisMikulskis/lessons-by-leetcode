class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        if low < 10 and high <= 10:
            return 0
        number, result_step = low, 0
        while number <= high:
            if len(str(number)) % 2 != 0:
                number = 11 if number < 100 else int(str(number) + '0')
            s = list(str(number))
            mid = len(s) // 2
            left_sum, right_sum = sum(map(int, s[:mid])), sum(map(int, s[mid:]))
            if left_sum == right_sum:
                result_step += 1
            number += 1
        return result_step


sol = Solution()
# sol.countSymmetricIntegers(1200, 12311143)
print(sol.countSymmetricIntegers(2, 11))
