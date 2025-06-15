class Solution:
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1], 2)


        # return int(int(''.join(list(reversed(str(n))))), 32)

sol = Solution()
print(sol.reverseBits(n = 964176192))
n = 43261596
print(bin(n))

