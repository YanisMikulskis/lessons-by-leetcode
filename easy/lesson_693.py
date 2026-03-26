class Solution:
    def hasAlternatingBits(self, n: int):

        bin_lst = list(bin(n)[2:])
        for i in range(len(bin_lst) - 1):
            if bin_lst[i] == bin_lst[i + 1]:
                return False
        return True

sol = Solution()
print(sol.hasAlternatingBits(10))