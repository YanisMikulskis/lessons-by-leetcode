class Solution:
    def numberOfComponents(self, properties: list[list[int]], k: int) -> int:
        res = []


        for i in range(len(properties)):
            for j in range(i + 1, len(properties)):
                res.append([set(properties[i]) & set(properties[j])])
        print(res)




sol = Solution()
sol.numberOfComponents(properties = [
  [10, 20, 30],
  [30, 40, 50],
  [50, 60, 70],
  [10, 70, 90]
],
k = 1)