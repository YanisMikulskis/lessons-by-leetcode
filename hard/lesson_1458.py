class Solution:
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:
        temporary = []
        temporary2 = []
        for num1 in range(len(nums1)):
            for num2 in range(num1 + 1, len(nums1) + 1):
                temporary.append(nums1[num1:num2])
        print(temporary)

        for num1 in range(len(nums1)):
            temp = [nums1[num1]]


sol = Solution()
sol.maxDotProduct([2,1,-2,5], [3,0,-6])