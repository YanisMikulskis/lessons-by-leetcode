class Solution:
    def kMirror(self, k: int, n: int) -> int:

        def check_palindrome(num):
            # if not num:
            #     return True
            # return check_palindrome(num[1:-1]) if num[0] == num[-1] else False
            return True if num == num[::-1] else False



        print(check_palindrome('1001'))
        print(check_palindrome('1000'))
        result = []
        def mutate_num(num, res):

            res.append(num % k)
        mutate_num(num=num, [])

sol = Solution()
sol.kMirror(k = 2, n = 5)