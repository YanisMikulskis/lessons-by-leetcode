class Solution:
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1], 2)




sol = Solution()
print(sol.reverseBits(n = 964176192))
n = 43261596
print(bin(n))

