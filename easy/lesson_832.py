class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:

        for l in range(len(image)):
            image[l].reverse()
            image[l] = list(map(lambda x: 0 if x == 1 else 1, image[l]))

        return image
sol = Solution()
sol.flipAndInvertImage([[1, 1, 0, 0],
                        [1, 0, 0, 1],
                        [0, 1, 1, 1],
                        [1, 0, 1, 0]])


