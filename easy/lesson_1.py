def task1():
    """
    1. Two Sum
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up
    to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    """

    def function(nums: list, target: int) -> list:
        visited = {

        }
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in visited:
                return [visited[complement], idx]
            else:
                visited.setdefault(num, idx)

    print(function([3, 3], 6))
    print(function([2, 7, 11, 15], 13))
    print(function([3, 2, 4], 6))
