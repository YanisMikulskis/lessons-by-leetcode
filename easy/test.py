import string
from string import ascii_uppercase as alp
from collections import deque
class Solution:


    def remainder_func(self, num):
        return 26 if num % 26 == 0 else num % 26

    def titleToNumber(self, columnTitle: str) -> int:
        temporary_deque = deque()
        alp_dict = {alp[let]: let + 1 for let in range(len(alp))}



    def convertToTitle(self, columnNumber: int) -> str:
        temporary_deque = deque()
        alp_dict = {let + 1:alp[let] for let in range(len(alp))}
        while columnNumber > 26:
            remainder = self.remainder_func(columnNumber)
            temporary_deque.appendleft(self.remainder_func(remainder))
            columnNumber = (columnNumber - remainder) // 26
        else:
            temporary_deque.appendleft(self.remainder_func(columnNumber))
        return ''.join([alp_dict[key] for key in temporary_deque])


sol = Solution()
sol.titleToNumber(...)
print(sol.convertToTitle(701))



#alghorithm for input: str
# def remainder_func(num):
#     return 26 if num % 26 == 0 else num % 26
#
#
# for num in range(1, 100):
#     column = num
#     temporary_deque = deque()
#     while num > 26:
#         remainder = remainder_func(num)
#         temporary_deque.appendleft(remainder_func(remainder))
#         num = (num - remainder) // 26
#     else:
#         temporary_deque.appendleft(remainder_func(num)))
#     # print(f'temp_deque = {temporary_deque}')
#     print(f"{''.join([alp_dict[k] for k in temporary_deque])} : {column}")