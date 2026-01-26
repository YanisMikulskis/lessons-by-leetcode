class Solution:
    def minBitwiseArray(self, nums):
        ans = []
        for i in nums:
            if i % 2 == 0:
                ans.append(-1)
            else:
                x = 0
                while x | x + 1 != i:
                    x += 1
                else:
                    ans.append(x)
        return ans


sol = Solution()
print(sol.minBitwiseArray([2,3,5,7]))


s = 'abcdef'
snew = ''
snew2 = ''.join([s[let] for let in range(len(s) - 1, -1, -1)])
print(snew2)
for let in range(len(s) - 1, -1, -1):
    snew += s[let]
print(snew)