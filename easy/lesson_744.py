class Solution:
    def nextGreatestLetter(self, letters, target) -> str:
        min_let = None
        for let in letters:
            if let > target:
                min_let = let if min_let is None or min_let > let else min_let

        return min_let if min_let else letters[0]

sol = Solution()
print(sol.nextGreatestLetter(letters = ["x","x","y","y"], target = "z"))