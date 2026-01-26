class Solution:
    '''
    1266. Минимальное время посещения всех точек
    На двумерной плоскости задано n точек с целочисленными координатами:
    points[i] = [xi, yi].
    Нужно найти минимальное время (в секундах), чтобы посетить все точки строго в том порядке, в
     котором они даны в массиве points.
    '''
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        time = 0
        for i in range(len(points) - 1):
            time += max(abs(points[i + 1][0] - points[i][0]), abs(points[i + 1][1] - points[i][1]))
        return time

sol = Solution()
print(sol.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))