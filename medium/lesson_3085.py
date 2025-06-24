from collections import Counter, defaultdict
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        # cnt = list(Counter(word).values())
        # print(Counter(word))
        # print(f'cnt = {cnt}')
        # self.temp = 0
        # def func_delta(arr, i, step, res):
        #
        #     if i + step == len(arr):
        #         i, step = i + 1, 1
        #
        #     if i == len(arr) - 1:
        #         return res
        #
        #     target = abs(arr[i] - arr[i + step])
        #     if target > k:
        #         self.temp += 1
        #     res.append(target - 1)
        #     return func_delta(arr, i, step + 1, res)
        #
        #
        #
        # result = func_delta(cnt, 0, 1, [])
        # print(result)
        # print(f'temp = {self.temp}')
        # print(sum(x > k for x in result))



    # def minimumDeletions(self, word: str, k: int) -> int:
    #
    #     def func_delta(arr, i, step, temp):
    #         print(arr)
    #         if len(arr) == 1:
    #             return 0
    #         if i + step == len(arr):
    #             i, step = i + 1, 1
    #
    #
    #         if i == len(arr) - 1:
    #             return temp
    #
    #         target = abs(arr[i] - arr[i + step])
    #         if target > k:
    #             print(f'tar = {target}')
    #             print(temp)
    #             temp += 1
    #             print(temp)
    #
    #         return func_delta(arr, i, step + 1, temp)
    #
    #     return func_delta(list(Counter(word).values()), 0, 1, 0)

        # for i in range(r)

        cnt = defaultdict(int)
        for c in word:
            cnt[c] += 1
        res = len(word)
        print(cnt.values())
        for a in cnt.values():
            deleted = 0
            for b in cnt.values():
                if a > b:
                    print(f'deleted1 after = {deleted}')
                    deleted += b
                    print(f'deleted2 before = {deleted}')
                    print()
                elif b > a + k:
                    print(f'deleted2 = {deleted}')
                    deleted += b - (a + k)
                    print(f'deleted22 = {deleted}')
                    print()

            res = min(res, deleted)
        return res

        # print(cnt)
        #
        # left, right = 0, 1
        # res = []
        # while left < len(cnt) - 1:
        #     res.append(abs(cnt[left] - cnt[right]))
        #     right += 1
        #     if right == len(cnt):
        #         left += 1
        #         right = left + 1
        # print(res)
        # res = list(map(lambda x: x - 1, res))
        # print(res)
        # #temp = [2, 3, 5]
        # temp = 0
        # while res:
        #     for i in range(len(res)):
        #         if res[i] > k:
        #             temp += 1
        #             res = [i for i in list(map(lambda x: x - 1, res)) if i > k]


sol = Solution()
# print(sol.minimumDeletions(word = "dabdcbdcdcd", k = 2))
# print(sol.minimumDeletions(word = "aabcaba", k = 0))
print('------')
# print(sol.minimumDeletions("aaabaaa", 2))
print('------')
# print(sol.minimumDeletions("ttt", 2))
print(sol.minimumDeletions("ahahnhahhah", 1)) #2
print(f'------')
# print(sol.minimumDeletions("aabbcc", 1))