class Solution:
    '''
    Условие
    Дана строка "PAYPALISHIRING", записанная в зигзагообразном порядке по заданному количеству строк. Например, если numRows = 3, строка записывается так:

    P   A   H   N
    A P L S I I G
    Y   I   R

    [P,A,Y][' ', P, ' '][A,L,I]
    Затем строка читается построчно, и получается "PAHNAPLSIIGYIR".

    Напишите функцию, которая выполняет такое преобразование:

    string convert(string s, int numRows);

    4. numRows = 4

    "PAYPALISHIRING"


    P     I    N
    A   L S  I G
    Y A   H R
    P     I
    Выход: "PINALSIGYAHRPI"
    [P A Y P] [' ', ' ', A, ' '] [' ', L, ' ', ' ']
    '''
    def convert(self, s: str, numRows: int) -> str:
        dinamic_lenght = lenght = 2 * (numRows - 1)
        print(f'len = {lenght}')
        print(lenght)
        res = [[]]
        #(2:2) (3:4) (4:6) (5:8) (6:10) (7:12) (8:14)
        result, vector = '', 'down'
        # result += f'{s[0]}{s[lenght]}'
        # result += f'{s[lenght + lenght]}'
        print(result)
        idx = 0
        for i in range(numRows):
            result += s[idx]
            while dinamic_lenght < len(s):
                result += s[dinamic_lenght]
                dinamic_lenght += lenght
            result += '  '
            idx += 1
            lenght -= 1
            dinamic_lenght = lenght - 1
            if lenght == 1:
                dinamic_lenght = lenght = 2 * (numRows - 1)
        print(result)





sol = Solution()

sol.convert(s = "PAYPALISHIRING",
numRows = 3)

# sol.convert(s = "PAYPALISHIRING",
# numRows = 4)
#
# sol.convert(s = "PAYPALISHIRING",
# numRows = 8)


