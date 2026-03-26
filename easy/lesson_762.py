from collections import Counter
class Solution:
    def countPrimeSetBits(self, left: int, right: int):
        easy_dict = {number:1 for number in [2,3,5,7,11,13,17,19]}
        ans = 0
        for i in range(left, right + 1):
            try:
                ans += easy_dict[Counter(bin(i)[2:])['1']]
            except KeyError:
                continue
        return ans



sol = Solution()
sol.countPrimeSetBits(10,15)