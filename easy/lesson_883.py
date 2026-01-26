import random


class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        xy = len([j for i in grid for j in i if j])
        zx = sum([max(i) for i in grid])
        l = len(grid[0])
        yz = sum([max([grid[j][i] for j in range(l)]) for i in range(l)])


        return xy + zx + yz

sol = Solution()

print(sol.projectionArea([[1,1,1],[1,0,1],[1,1,1]]))


#
# arr = [1,2,3,4,5,6,67]
#
# arr_random = list(range(random.randint(1,100)))
# print(arr_random)
#
# max1 = 0
# max2 = 0
#
# for i in arr_random:
#     if i > max1:
#         max2 = max1
#         max1 = i
#     if max1 > i > max2:
