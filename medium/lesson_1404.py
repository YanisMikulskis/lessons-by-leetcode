class Solution:
    def numSteps(self, s: str) -> int:
        def bin_decimal(number):
            ans, n = 0, len(number)
            for i in range(n):
                ans += int(number[i]) * (2 ** (n - i - 1))
            return ans
        step, ans = 0, bin_decimal(s)
        while ans != 1:
            ans = ans + 1 if ans % 2 != 0 else ans // 2
            step += 1
        return step


sol = Solution()
print(sol.numSteps("10"))