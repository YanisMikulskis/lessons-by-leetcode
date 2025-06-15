class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        def check():

            honest_sum = sum([int(num[i]) for i in range(len(num)) if i % 2 == 0])
            no_honest_sum = sum([int(num[i]) for i in range(len(num)) if i % 2 != 0])
            if honest_sum == no_honest_sum:
                return True
            return False



sol = Solution()
sol.countBalancedPermutations('123')