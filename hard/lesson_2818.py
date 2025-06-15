class Solution:
    '''
    You are given an array nums of n positive integers and an integer k.

    Initially, you start with a score of 1. You have to maximize your score by applying
    the following operation at most k times:

    Choose any non-empty subarray nums[l, ..., r] that you haven't chosen previously.
    Choose an element x of nums[l, ..., r] with the highest prime score. If multiple such
    elements exist, choose the one with the smallest index.
    Multiply your score by x.
    Here, nums[l, ..., r] denotes the subarray of nums starting at index l and ending at the
     index r, both ends being inclusive.

    The prime score of an integer x is equal to the number of distinct prime factors of x.
    For example, the prime score of 300 is 3 since 300 = 2 * 2 * 3 * 5 * 5.

    Return the maximum possible score after applying at most k operations.

    Since the answer may be large, return it modulo 109 + 7.


    Example 1:

    Input: nums = [8,3,9,3,8], k = 2
    Output: 81
    Explanation: To get a score of 81, we can apply the following operations:
    - Choose subarray nums[2, ..., 2]. nums[2] is the only element in this subarray.
    Hence, we multiply the score by nums[2]. The score becomes 1 * 9 = 9.
    - Choose subarray nums[2, ..., 3]. Both nums[2] and nums[3] have a prime score of 1,
    but nums[2] has the smaller index. Hence, we multiply the score by nums[2]. The score becomes 9 * 9 = 81.
    It can be proven that 81 is the highest score one can obtain.


    '''
    def maximumScore(self, nums: list[int], k: int) -> int:
        # score = 1
        #
        # def prime_factor(number, factors):
        #     mul = 2
        #     while number != 1:
        #         if number % mul == 0:
        #             number //= mul
        #             factors.append(mul)
        #         else:
        #             mul += 1
        #     return factors
        #
        # scores_dict = [[i, len(set(prime_factor(nums[i], []))), nums[i]] for i in range(len(nums))]
        #
        # for i in range(k):
        #     max_score = max(scores_dict, key=lambda x:x[2])
        #     idx = max_score[0]
        #     results.append(max_score)
        #     # scores_dict.pop(idx)
        #     score *= max_score[2]
        #     scores_dict = list(map(lambda x: [x[0] - 1 if x[0] > idx else x[0], x[1], x[2]],scores_dict))
        # return score
        #
        # # for i in range(k):
        # #     print(scores_dict)
        # #     max_score = max(scores_dict, key=lambda x:max(scores_dict[x][0]))
        # #     print(scores_dict.pop(max_score))

        class Solution:
            MOD = 10 ** 9 + 7

            def maximumScore(self, nums, k):
                n = len(nums)
                prime_scores = [0] * n

                # Calculate the prime score for each number in nums
                for index in range(n):
                    num = nums[index]

                    # Check for prime factors from 2 to sqrt(n)
                    for factor in range(2, int(math.sqrt(num)) + 1):
                        if num % factor == 0:
                            # Increment prime score for each prime factor
                            prime_scores[index] += 1

                            # Remove all occurrences of the prime factor from num
                            while num % factor == 0:
                                num //= factor

                    # If num is still greater than or equal to 2, it's a prime factor
                    if num >= 2:
                        prime_scores[index] += 1

                # Initialize next and previous dominant index arrays
                next_dominant = [n] * n
                prev_dominant = [-1] * n

                # Stack to store indices for monotonic decreasing prime score
                decreasing_prime_score_stack = []

                # Calculate the next and previous dominant indices for each number
                for index in range(n):
                    # While the stack is not empty and the current prime score is greater than the stack's top
                    while (
                            decreasing_prime_score_stack
                            and prime_scores[decreasing_prime_score_stack[-1]]
                            < prime_scores[index]
                    ):
                        top_index = decreasing_prime_score_stack.pop()

                        # Set the next dominant element for the popped index
                        next_dominant[top_index] = index

                    # If the stack is not empty, set the previous dominant element for the current index
                    if decreasing_prime_score_stack:
                        prev_dominant[index] = decreasing_prime_score_stack[-1]

                    # Push the current index onto the stack
                    decreasing_prime_score_stack.append(index)

                # Calculate the number of subarrays in which each element is dominant
                num_of_subarrays = [0] * n
                for index in range(n):
                    num_of_subarrays[index] = (next_dominant[index] - index) * (
                            index - prev_dominant[index]
                    )

                # Priority queue to process elements in decreasing order of their value
                processing_queue = []

                # Push each number and its index onto the priority queue
                for index in range(n):
                    heapq.heappush(processing_queue, (-nums[index], index))

                score = 1

                # Helper function to compute the power of a number modulo MOD
                def _power(base, exponent):
                    res = 1

                    # Calculate the exponentiation using binary exponentiation
                    while exponent > 0:
                        # If the exponent is odd, multiply the result by the base
                        if exponent % 2 == 1:
                            res = (res * base) % self.MOD

                        # Square the base and halve the exponent
                        base = (base * base) % self.MOD
                        exponent //= 2

                    return res

                # Process elements while there are operations left
                while k > 0:
                    # Get the element with the maximum value from the queue
                    num, index = heapq.heappop(processing_queue)
                    num = -num  # Negate back to positive

                    # Calculate the number of operations to apply on the current element
                    operations = min(k, num_of_subarrays[index])

                    # Update the score by raising the element to the power of operations
                    score = (score * _power(num, operations)) % self.MOD

                    # Reduce the remaining operations count
                    k -= operations

                return score




        # print(prime_factor(128, factors=[]))
sol = Solution()
sol.maximumScore(nums = [19,12,14,6,10,18], k = 3)
print(f'-------')
# sol.maximumScore(nums = [8,3,9,3,8], k = 2)
# arr = [[[19], 19], [[2, 2, 3], 12], [[2, 700], 14]]
# print(max(arr, key=lambda x:max(x[0])))