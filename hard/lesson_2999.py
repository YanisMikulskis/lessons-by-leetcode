class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        if int(s) > finish:
            return 0
        # избавляемся от ненужной части последовательности, находим максимально возможную границу (делаем финиш)
        finish_lst = list(map(int, str(finish)))
        left = finish_lst[:-len(s)]
        # suffix_int = ''.join(map(str, finish_lst[-len(s):]))

        for num in range(len(left)):
            if left[num] > limit:
                left[num] = limit
        else:
            left = ''.join(map(str, left))

        finish_copy = finish
        if int(left + s) < finish_copy:
            finish = int(left + s)




        # делаем минимально допустимый старт
        if start < int(s):
            start = int(s)
        print(f'start = {start}')
        print(f'finish = {finish}')
        #-------------------------
        result = []
        for num in range(start, finish + 1):
            left = str(num)[:-len(s)]
            if not all([int(i) <= limit for i in left]):
                continue


            suffix = str(num)[-len(s):]

            if suffix != s:
                continue
            result.append(num)
        return len(result)









sol = Solution()
print(sol.numberOfPowerfulInt(start = 1, finish = 6000, limit = 4, s = "124"))
print(f'----')
print(sol.numberOfPowerfulInt(start = 15, finish = 215, limit = 6, s = "10"))
print(f'----')
print(sol.numberOfPowerfulInt(start = 1000, finish = 2000, limit = 4, s = "3000"))
print(f'----')
print(sol.numberOfPowerfulInt(141, 148, 9, '9'))
print(f'----')