from collections import Counter
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        def freq(sub):
            cnt = Counter(sub)
            a1, a2 = float('-inf'), float('inf')
            for num in cnt:
                if cnt[num] % 2 != 0 and cnt[num] > a1:
                    a1 = cnt[num]
                    continue
                if cnt[num] % 2 == 0 and cnt[num] < a2:
                    a2 = cnt[num]
            return 0 if a1 == float('-inf') or a2 == float('inf') else a1 - a2

        def make_subs(s, left, step, result):

            if step == len(s) + 1:
                left += 1
                step = left + k

            if step > len(s):
                return result

            temp = freq(s[left:step])
            if temp and temp > result:
                result = temp
            return make_subs(s, left, step + 1, result)
        return make_subs(s,0, k, float('-inf'))