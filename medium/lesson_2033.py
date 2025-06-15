import numpy as np
class Solution:
    '''
    Условие
    Дан двумерный массив (сетка) grid размером m × n и число x.

    За одну операцию можно:

    Прибавить x к любому элементу сетки.
    Вычесть x из любого элемента сетки.
    ⚡ Определите минимальное количество операций, чтобы все элементы стали одинаковыми.
    Если это невозможно, верните -1.
    '''
    def minOperations(self, grid: list[list[int]], x: int) -> int:

        lst = [j for i in grid for j in i]
        lst.sort()

        med = (len(lst) // 2) - 1 if len(lst) % 2 == 0 else len(lst) // 2
        middle, result = lst.pop(med), 0

        for i in lst:
            delta = abs(middle - i)
            if delta % x == 0:
                result += delta // x
            else:
                return -1
        return result
        # for i in lst:
        #     if i < middle:
        #         while i < middle:
        #             i += x
        #             result += 1
        #         else:
        #             if i > middle:
        #                 return -1
        #     else:
        #         while i > middle:
        #             i -= x
        #             result += 1
        #         else:
        #             if i < middle:
        #                 return -1
        # return result



# sol = Solution()
# print(sol.minOperations(grid = [[2,4],[6,8]], x = 2))
# print(sol.minOperations(grid = [[1,5],[2,3]], x = 1))

DATA = {'csrfmiddlewaretoken': 'zvs7go_h_q_rjq_sh6_am8_b_a_y62_nmk_g6y_f_p_i_l_jpzi67m_g_z67_ai_kyw_vtmm_w7faf_zpsxp_s_g',
        'name': 'lflsfdl', 'url_repo': 'http://mail.yandex.ru/?win=27&clid=41128',
        'users': '6'}

csrf_token = {'csrfmiddlewaretoken': DATA['csrfmiddlewaretoken']}
DATA.pop('csrfmiddlewaretoken')
print(csrf_token)
print(DATA)

ssse = 'camel_case'
print(''.join(map(lambda x:x[0].upper() + x[1:] ,ssse.split('_'))))
