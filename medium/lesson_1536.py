from collections import Counter
class Solution:
    def minSwaps(self, grid):
        n = len(grid)
        def check(grid):
            for line in range(1, n):
                if Counter([column[line] for column in grid])[0] < line:
                    return -1
            return True

        zeros = n - 1
        border = 1
        ans = 0
        while border <= n + 1:
            for i in grid:
                print(i)
            print(f'------')
            for i in range(border - 1, n):
                if Counter(grid[i][border:])[0] == zeros:
                    ans += i - border + 1
                    grid[i], grid[border - 1] = grid[border - 1], grid[i]
                    border += 1
                    zeros -= 1
                    continue

sol = Solution()
sol.minSwaps([[0,0,1],
              [1,1,0],
              [1,0,0]])