
from string import ascii_lowercase
class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        n = len(strs[0])
        if n == 0:
            return 0

        column, ans, elem = 0, 0, 0

        while elem < len(strs) - 1:

            if not strs[elem]:
                return ans


            if strs[elem][column] == strs[elem + 1][column]:
                if column < len(strs[elem]) - 1:
                    column += 1
                else:
                    elem += 1

            elif strs[elem][column] > strs[elem + 1][column]:
                ans += 1
                strs = [f'{item[:column]}{item[column + 1:]}'for item in strs]
                column = 0
                elem = 0
            else:
                column = 0
                elem += 1

        return ans
sol = Solution()
print(ascii_lowercase)
# print(sol.minDeletionSize(strs = ["xc","yb","za"]))
print(sol.minDeletionSize(strs = ["vdy","vei","zvc","zld"]))