class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans = 0
        MOD = 10**9 + 7
        for i in range(1, n + 1):
            ans = ((ans << i.bit_length()) | i) % MOD
        return ans

sol = Solution()
print(sol.concatenatedBinary(n = 12))