class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        for let in range(len(s)):
            print(s[let:let + 2])
            if s[let:let + 1] == '01':
                return False
        return True

sol = Solution()
print(sol.checkOnesSegment('1001'))