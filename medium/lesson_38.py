class Solution:
    def countAndSay(self, n: int) -> str:

        def func(s):
            res = [[1, s[0]]]
            for i in s[1:]:
                if i == res[-1][1]:
                    res[-1][0] += 1
                else:
                    res.append([1, i])
            return ''.join([''.join(list(map(str, i))) for i in res])


        start = '1'
        for _ in range(n - 1):
            start = func(start)
        return start







sol = Solution()
print(sol.countAndSay(4))