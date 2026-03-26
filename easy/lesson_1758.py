class Solution:
    def minOperations(self, s: str):
        def func(mask, ans):
            for elem in range(len(s)):
                if s[elem] != mask:
                    ans += 1
                mask = '1' if mask == '0' else '0'
            return ans
        return min(func('0', 0), func('1', 0))





sol = Solution()
sol.minOperations("111000111")