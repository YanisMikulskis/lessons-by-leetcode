import math




nums = [21,4,7]



class Solution:
    def sumFourDivisors(self, nums: list[int]):


        def check(n):
            total = 1 + n
            count = 0

            for i in range(2, math.isqrt(n) + 1):
                if n % i == 0:
                    other = n // i
                    if other == i:
                        return 0
                    count += 2
                    total += i + (n // i)
                    if count > 2:
                        return 0
            return total if count == 2 else 0


        return sum(check(n) for n in nums)
sol = Solution()
print(sol.sumFourDivisors([21, 4, 7]))
#
#
# print(math.isqrt(21))

