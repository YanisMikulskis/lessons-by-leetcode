class Solution:
    '''
    Даны два целых числа: n и k.

    Вернуть k-й по счёту элемент в лексикографическом порядке среди всех чисел от 1 до n включительно.

    ℹ️ Что такое лексикографический порядок?
    Это порядок, как в словаре. То есть числа сравниваются как строки.

    Примеры:

    1 < 10 < 100 < 101 < 102 < 11 < 12 < 2 < 3 < ... < 9
    🧮 Примеры:
    Пример 1:

    n = 13, k = 2
    Числа от 1 до 13 в лексикографическом порядке:

    1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9
    2-е число в этом порядке → 10

    Ответ: 10
    '''
    def findKthNumber(self, n: int, k: int) -> int:
        # lex_nums = list(sorted(map(str, range(1, n + 1))))
        # print(lex_nums)
        # # ans = '1'
        # # new_res = []
        # # while len(new_res) < k:
        # #     new_res += [ans]
        # #     ans = str(int(ans) + 1)
        # #     new_res.sort()
        class Tree:
            def __init__(self, core):
                self.core = core
                self.left,self.right = None, None
            def make_branch(self, element):
                if element < self.core:
                    if self.left is None:
                        self.left = Tree(element)
                    else:
                        self.left.make_branch(element)
                else:
                    if self.right is None:
                        self.right = Tree(element)
                    else:
                        self.right.make_branch(element)


sol = Solution()
sol.findKthNumber(120,5)