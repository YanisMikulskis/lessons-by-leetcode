class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return sum([n for n in range(1, n + 1) if n % m != 0]) - sum([n for n in range(1, n + 1) if n % m == 0])
