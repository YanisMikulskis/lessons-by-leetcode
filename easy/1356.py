from collections import Counter
class Solution:
    def sortByBits(self, arr):
        print([bin(i)[2:] for i in arr])


        #
        # new_res = [arr.pop(0)]
        #
        # i = 0
        # idx = -1
        # while arr:
        #     print(f'new_res = {new_res}')
        #     elem = arr.pop(0)
        #     if elem < arr[idx]:
        #         idx -= 1
        #     else:
        #         new_res.insert(idx, elem)
        #         idx = -1




        result = []
        d = {
        }
        for num in arr:
            units = Counter(bin(num)[2:])['1']
            if units not in d:
                d[units] = []
            d[units].append(num)
        else:
            for k,v in dict(sorted(d.items())).items():
                v.sort()
                result += v
        return result








sol = Solution()
print(sol.sortByBits([10,100,1000,10000]))