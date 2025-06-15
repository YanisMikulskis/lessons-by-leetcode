import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        variable_symbols = string.ascii_lowercase + ''.join(list(map(str, range(10))))
        def mutate_string(s):
            return ''.join([let.lower() for let in s if let.lower() in variable_symbols])
        new_str = mutate_string(s)
        def check_palindrom(s):
            return s == s[::-1]
        print(check_palindrom(new_str))

sol = Solution()
sol.isPalindrome(s = "A man, a plan, a canal: Panama")