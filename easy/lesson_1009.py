class Solution:
    def bitwiseComplement(self, n: int) -> int:

        bin_n = bin(n)[2:]
        new_n = 0
        for i in bin_n)):
            if bin_n[i] == '0':
                new_n += 1 * (2**(len(bin_n) - i - 1))


        return n
sol = Solution()
sol.bitwiseComplement(10)