# class Solution:
#     def bestClosingTime(self, customers: str):
#         close = 0
#         dp = {
#         }
#         while close <= len(customers):
#             fine_temp = 0
#             for day in range(len(customers)):
#                 if day < close: # день, когда магазин еще открыт
#                     if customers[day] == 'N':
#                         fine_temp += 1
#                 else: # день, когда магазин уже закрыт
#                     if customers[day] == 'Y':
#                         fine_temp += 1
#             print(f'Если магазин закрывает в {close}-й день, то штраф составит {fine_temp}')
#
#             if fine_temp == 0 or fine_temp == 1: # если штрафов нет либо штраф равен 1 (минимальный) -
#                                                     # сразу возвращаем первый день
#                 return close
#
#             if fine_temp not in dp:
#                 dp[fine_temp] = []
#             dp[fine_temp].append(close)
#             close += 1
#         for f,d in dp.items():
#             print(f'Штраф размером {f} будет, если закрыть магазин в {d} дни')
#         return min(dp[min(dp)])
#
#
#
#
#
# sol = Solution()
# print(sol.bestClosingTime('YYNY'))


from collections import Counter
class Solution:
    def bestClosingTime(self, customers: str):
        start = Counter(customers)['Y']
        min_start, result_hour = start, 0
        if not start:
            return start

        for hour in range(len(customers)):
            if customers[hour] == 'Y':
                start -= 1
            else:
                start += 1
            if start < min_start:
                min_start, result_hour = start, hour + 1

        return result_hour




sol = Solution()
print(sol.bestClosingTime("YYYY"))





