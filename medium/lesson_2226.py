class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        left, right = 0, max(candies)
        result = 0

        while left <= right:
            mid = (left + right) // 2

            count = sum([c // mid for c in candies])
            if count >= k:
                result = mid
                left = mid + 1
            else:
                right = mid -1
        return result





        # while var < 5:
        #     print(var)
        #     for i in range(len(candies)):
        #         if candies[i]:
        #             candies[i] -= 1
        #     print(f'cand = {candies}')
        #     res += 1
        #     var += 1







sol = Solution()
print(sol.maximumCandies(candies = [5,8,6], k = 3))# => 5
sol.maximumCandies(candies = [2,5], k = 11)
# sol.maximumCandies(candies=[2,5,7,10], k = 4) #=> 5
# # print(f'------')
# sol.maximumCandies(candies = [1, 2, 3, 4, 10], k = 5)# => 2
