from collections import Counter
class Solution:
    '''
    У нас есть неориентированный граф с n вершинами, пронумерованными от 0 до n - 1. Также даны edges, где edges[i] = [ui, vi] означает, что существует ребро между вершинами ui и vi.

    Нужно посчитать количество "полных компонентов" в этом графе.

    Что такое "полный компонент" (Complete Component)?
    Компонент связности называется "полным", если:

    Все вершины соединены друг с другом.
    То есть в компоненте каждая вершина соединена с каждой другой.
    Нет "изолированных" пар вершин, которые не соединены ребром.
    Задача
    Найти количество полных компонент в данном графе.

    Примеры с объяснениями

    Пример 1
    Входные данные:

    n = 6
    edges = [[0, 1], [0, 2], [1, 2], [3, 4]]
    Разбираем граф:

    Вершины {0, 1, 2} образуют полный компонент, потому что каждая соединена с каждой другой.
    Вершины {3, 4} образуют неполный компонент, так как не хватает 5.
    Вершина 5 изолирована (не соединена ни с кем) и тоже считается "полным компонентом".
    Визуализация графа:

      0 ---- 1
       \    /
        \  /
          2       3 --- 4    5
    Результат:

    2 (компоненты: {0,1,2} и {5})

    '''
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:

        cores = list(set([j for i in edges for j in i]))
        print(cores)
        alone_cores = 0
        if n > len(edges):
            alone_cores = n - 1 - len(edges)
        print(alone_cores)
        left, right = edges[0][0], edges[0][1]
        idx = 0
        res = [[]]
        while any(edges):
            if idx == len(edges):
                idx = 0
                res.append([])
                for i in edges:
                    if i:
                        left, right = i

            if edges[idx]:
                if left in edges[idx]:
                    res[-1].append(edges[idx])
                    left = edges[idx][0]
                    edges[idx] = 0

                elif right in edges[idx]:
                    # if edges[idx] not in res[-1]:
                    res[-1].append(edges[idx])
                    right = edges[idx][1]
                    edges[idx] = 0

            idx += 1

        print(res)
        combs = [Counter([item for elem in i for item in elem]) for i in res]
        print(combs)
        count_comp = 0
        for i in combs:
            if list(i.values()).count(1) == len(i.values()) or all([item >= 2 for item in i.values()]):
                count_comp += 1
        print(count_comp + alone_cores)
        return count_comp + alone_cores







sol = Solution()
# sol.countCompleteComponents(n = 6, edges = [[0,1],[0,2],[1,2],[3,4]])
# sol.countCompleteComponents(n = 6, edges = [[0, 1], [0, 2], [1, 2], [3, 4],[6,7], [5,6], [5,7]])
# sol.countCompleteComponents(n = 6, edges = [[0, 1], [0, 3], [1, 2], [2, 3]])
# sol.countCompleteComponents(n = 6, edges = [[0,1],[0,2],[1,2],[3,4]])
# sol.countCompleteComponents(n=6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]])
# sol.countCompleteComponents(n = 10, edges=[[0, 1], [0, 2]])
# sol.countCompleteComponents(n=3, edges=[[2,0]])
# sol.countCompleteComponents(n = 5, edges = [[1,2],[3,4],[1,4],[2,3],[1,3],[2,4]])
import heapq

arr = [(0, 10), (2,3)]

print(heapq.heappop(arr))


def dijkstra(graph, start):
    # # Инициализация словаря для хранения расстояний
    # # до каждой вершины. Сначала все расстояния бесконечны.
    # distances = {vertex: float('infinity') for vertex in graph}
    #
    # # Расстояние до начальной вершины равно 0.
    # distances[start] = 0
    #
    #
    # # Создаём приоритетную очередь для хранения вершин и их расстояний.
    # priority_queue = [(0, start)]
    # while priority_queue:
    #     # Извлекаем вершину с наименьшим расстоянием из очереди.
    #     current_distance, current_vertex = heapq.heappop(priority_queue)
    #
    #
    #     # Если текущее расстояние до вершины уже больше, чем сохранённое расстояние, игнорируем её.
    #     if current_distance > distances[current_vertex]:
    #         continue
    #
    #     # Рассмотрим все соседние вершины текущей вершины.
    #     for neighbor, weight in graph[current_vertex].items():
    #         distance = current_distance + weight
    #         # Если найден более короткий путь до соседа, обновим расстояние.
    #         if distance < distances[neighbor]:
    #             distances[neighbor] = distance
    #             heapq.heappush(priority_queue, (distance, neighbor))
    #
    # print(f'--------')
    # return distances

    distances = {core:float('infinity') for core in graph.keys()}
    distances[start] = 0




    print(distances)





print(dijkstra(graph={
    'A': {'B': 4, 'C': 7},
    'B': {'A': 4, 'D': 2, 'E': 8},
    'C': {'A': 7, 'D': 2, 'E': 5},
    'D': {'B': 2, 'C': 2, 'E': 1, 'F': 4},
    'E': {'C': 5, 'D': 1, 'F': 11},
    'F': {'B': 8, 'D': 4, 'E': 11}
}, start='A'))