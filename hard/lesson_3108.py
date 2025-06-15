class Solution:
    '''
    3108. Минимальная стоимость пути во взвешенном графе формулируется следующим образом:
    Дан неориентированный взвешенный граф с n вершинами, пронумерованными от 0 до n - 1.
    Вам предоставлены целое число n и массив edges, где edges[i] = [uᵢ, vᵢ, wᵢ] указывает на
    существование ребра между вершинами uᵢ и vᵢ с весом wᵢ.

    Прогулка (walk) в графе — это последовательность вершин и рёбер. Стоимость прогулки, начинающейся
    в вершине u и заканчивающейся в вершине v, определяется как побитовая операция AND над весами рёбер,
    пройденных во время прогулки. Иными словами, если последовательность весов рёбер, встреченных во время
    прогулки, это w₀, w₁, w₂, ..., wₖ, то стоимость вычисляется как w₀ & w₁ & w₂ & ... & wₖ,
    где & обозначает побитовую операцию AND.

    Вам также предоставлен двумерный массив query, где query[i] = [sᵢ, tᵢ]. Для каждого запроса
    необходимо найти минимальную стоимость прогулки, начинающейся в вершине sᵢ и заканчивающейся
    в вершине tᵢ. Если такой прогулки не существует, вернуть -1.

    Необходимо вернуть массив answer, где answer[i] обозначает минимальную стоимость
    прогулки для запроса i.
    '''
    def minimumCost(self, n: int, edges: list[list[int]], query: list[list[int]]) -> list[int]:
        # graph = {
        #
        # }
        #
        # for core in edges:
        #     if (core[0], core[1]) not in graph:
        #         graph.setdefault((core[0], core[1]))
        #     graph[(core[0], core[1])] = core[2]
        # print(graph)
        # walks = []
        # graph_copy = graph.copy()
        # graph_copy[100] = 0


        edges_copy = edges.copy()





        resa = []
        points_dict = {

        }

        for i in edges:
            points_dict.setdefault(i[0], []) if i[0] not in points_dict else ...
            points_dict[i[0]].append([i[1], i[2]])

        print(points_dict)

        way = list(range(query[0][0], query[0][1]))
        way_copy = way.copy()
        print(way)
        #
        print(edges_copy)
        while edges_copy:
            for i in range(len(way_copy)):
                for j in range(len(edges_copy)):
                    if way_copy[i] == edges_copy[j][0]



        # for w in query:
        #     way = list(range(w[0], w[1]))
        #     print(f'way = {way}')
        #     for p in range(len(edges_copy)):
        #         if edges_copy[p][0] in way and edges_copy[p] not in resa:
        #             resa.append(edges_copy[p])
        #             p -= 1
        #     print(resa)



            # while 1:
            #     way =
            #     way = [graph[(i, i + 1)] for i in range(w[0], w[1])]
            #     print(way)








sol = Solution()
# sol.minimumCost(
#                 n = 4,
#                 edges=[[0, 1, 2], [1, 2, 4], [2, 3, 8], [3, 0, 16]],
#                 query=[[0, 2], [0, 3], [1, 3], [2, 0]]
# )
#
#
# sol.minimumCost(n = 5,
#                 edges = [[0, 1, 7], [1, 2, 5], [0, 2, 2], [2, 3, 3], [3, 4, 1], [1, 4, 6]],
#                 query = [[0, 4]])

sol.minimumCost(n=5,
                edges=[[0, 1, 7], [1, 2, 5], [0, 2, 2], [2, 3, 3], [3, 4, 1], [1, 4, 6]],
                query = [[0, 4]])

#[0, 1, 7], [1, 2, 5],[2, 3, 3],[3, 4, 1]
#[0, 2, 2], [2, 3, 3], [3, 4, 1],
#[1, 4, 6]