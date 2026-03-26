class Solution:
    def minimumCost(self, source, target, original, changed, cost):
        ans = 0
        d = {

        }
        cost_idx = 0
        for i in zip(original, changed):
            coup = ''.join(list(i))
            if coup not in d:
                d[coup] = []
            d[coup].append(cost[cost_idx])
            cost_idx += 1
        print(d)
        print(d)
        def row(x,y):
            ans = 0
            d


        row('a','b')

sol = Solution()
sol.minimumCost(source = "aaaa",
                target = "bbbb",
                original = ["a","c", "a"],
                changed =  ["c","b", "c"],
                cost = [1,2, 5])