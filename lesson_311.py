def task1():
    """
    Задача: 311. Sparse Matrix Multiplication
    Даны две разреженные матрицы mat1 размером m x k и mat2 размером k x n.
    Верните результат перемножения матриц mat1 x mat2. Вы можете предположить, что умножение всегда возможно.
    """
    # Input: mat1 = [[1, 0, 0],
    #                [-1, 0, 3]],

    #        mat2 = [[7, 0, 0],
    #                [0, 0, 0],
    #                [0, 0, 1]]
    # Output: [[7, 0, 0],
    #          [-7, 0, 3]]
    # первая строка умножается поэлементо на первый столбец
    # первая строка умножается поэлементо на второй столбец
    # первая строка умножается поэлементо на третий столбец
    # второя строка умножается поэлементо на первый столбец
    # и тд

    mat1 = [[1, 0, 0],
            [-1, 0, 3]]

    mat2 = [[7, 0, 0],
            [0, 0, 0],
            [0, 0, 1]]



    def mul_matrix(mat1, mat2):
        def mul_recursion(idx1, idx2, point1, point2, new_mat):
            if idx2 == 0 and point2 == len(mat2[idx2]):
                return [sum(item) for item in new_mat]
            mul_result = mat1[idx1][point1] * mat2[idx2][point2]
            new_mat[-1].append(mul_result)
            if idx2 == len(mat2) - 1:
                new_mat.append([]) if len(new_mat) < len(mat2) else ...
                return mul_recursion(idx1, idx2=0, point1=0, point2=point2 + 1, new_mat=new_mat)
            return mul_recursion(idx1, idx2 + 1, point1 + 1, point2, new_mat)

        result = [mul_recursion(idx1=line, idx2=0, point1=0, point2=0, new_mat=[[]]) for line in range(len(mat1))]
        return result

    print(mul_matrix(mat1=mat1, mat2=mat2))
task1()