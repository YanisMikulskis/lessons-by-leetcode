class Solution:
    def countBinarySubstrings(self, s: str):
        i, j, ans = 0, 2, 0
        while i < len(s) - 1:
            if j == len(s) + 1:
                i, j = i + 1, i + 2
            sub = s[i:j]
            if len(sub) % 2 == 0:

                left, right = sub[:len(sub)//2], sub[len(sub)//2:]
                if left == '0' * (len(sub)//2) and right == '1' * (len(sub)//2) \
                    or left == '1' * (len(sub)//2) and right == '0' * (len(sub)//2):
                    print(f'sub = {sub}')
                    ans += 1
            j += 1

        return ans

for i in xra


sol = Solution()
print(sol.countBinarySubstrings(s = "10101"))