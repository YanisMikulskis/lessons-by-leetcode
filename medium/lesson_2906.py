class Solution:
    def constructProductMatrix(self, grid):
        n = len(grid)
        m = len(grid[0])
        dp2 = [[] for _ in range(n)]
        grid = [j for i in grid for j in i]
        i = 0
        ans = 1
        new_grid = []
        while i < len(grid):
            for elem in range(len(grid)):
                if elem != i:
                    ans *= grid[elem]
            ans %= 12345
            new_grid.append(ans)
            ans = 1
            i += 1
        step = 0
        for i in range(n):
            for _ in range(m):
                dp2[i].append(new_grid[step])
                step += 1


        return dp2



sol = Solution()
# print(sol.constructProductMatrix([[1,2],[3,4]]))
print(sol.constructProductMatrix([[12345],[2],[1]]))