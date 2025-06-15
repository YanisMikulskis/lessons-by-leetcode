class Solution:
    def minTimeToReach(self, moveTime: list[list[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])

        cord = [[f'{i}{j}' for j in range(m)] for i in range(n)]
        for i in cord:
            print(i)
        graph = {

        }

        for i in cord:
            [graph.setdefault(j,[]) for j in i]
        print(graph)
        line, column = 0,0

        def left(line, column):
            graph[f'{line}{column}'].append(f'{line}{column - 1}')
        def down(line, column):
            graph[f'{line}{column}'].append(f'{line + 1}{column}')
        def right(line, column):
            graph[f'{line}{column}'].append(f'{line}{column + 1}')
        def up(line, column):
            graph[f'{line}{column}'].append(f'{line - 1}{column}')

        while line < n - 1:

            if column == m:
                break
            if column == 0:
                right(line, column), down(line,column)
            elif 0 < column < m - 1:
                left(line, column), down(line, column), right(line, column)
            else:
                left(line, column), down(line, column)
            column += 1

        print(graph)





sol = Solution()
sol.minTimeToReach([[0, 4, 3],
                    [4, 4, 5]])


sol.minTimeToReach([[]])

