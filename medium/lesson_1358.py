class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        freq = {
        'a':0,
        'b':0,
        'c':0
        }
        result = 0
        point,start = 0,0
        if len(s) <= 1000:
            while start < len(s) - 1:
                if point == len(s):
                    freq = {'a': 0, 'b': 0, 'c': 0}
                    start += 1
                    point = start
                freq[s[point]] += 1
                if all(freq.values()):
                    result += 1
                point += 1
            return result
        else:
            return self.many_elements(s)

    def many_elements(self, s):
        rems = []
        while len(s) > 0:
            part = s[:3]
            rems.append(part)
            s = s[3:]
        print(rems)
        return [self.numberOfSubstrings(i) for i in rems]





sol = Solution()
print(sol.numberOfSubstrings(s='abcabc'))
# sol.numberOfSubstrings("aaacb")
# sol.numberOfSubstrings("abc")
# print(sol.numberOfSubstrings('cabbbaccaaacaacbaacaacabbbaaacababccaaccabacccbbacabcbccccccbaccbbbcbcccbaaaabcb'
#                        'cbbbcacacccbcbacbcbbcbaaacabacbcbbabbaacccbccabbcabaacababbaaaabcbbcccabaccacaaacbbcbaaab'
#                        'caaabacccbcbacbcccbaaabaaaababcbabaacbcacacbbbacbcaccbcabcbcaaaaaaababacaabacaacabcacaccabac'
#                        'cbcbacbaabbcbbbacaabcbacabacbaccabbbabbacaabcbaaacbcccacbaaacccbbcbcaaccbacbcaaccbcaaba'
#                        'abcbaacbbaaacbaabbcacbcbbcbbacbcaaaacbaabcabcaacbababccabcbaccabcbbbbbbbabbccaaabbaacbcccba'
#                        'accabccabbcbacccabbbbcbccaccccccaabcababcabccccaacccbabaccabbcabbbbbbaccacccacabaaaccaccc'
#                        'ccccbcccaccaabbcaabcabcaabaccaccbcabcacabbbcccccccbaacacababaacacaacacbbcabbbbcbbaabcbbaaca'
#                        'acccbaabbaabbacaacabacaabccbabcccabbbcbbccacaaaaaaaccccbbcaabccacaaaabacbabbbcbabacababbab'
#                        'babbbcabbccbbabbcccccbbccbacbaacbcababacbcbaaccbabccbcbabacccaacbabbbbccbcbcabbbcaabcbacbaac'
#                        'abaacabaacabaccbaabcacabaaacaccacabaacbcaacbccaaacbbaabcabbcccaabaccbcbaccaabaaacabbbcbcababbb'
#                        'caabbcaacaabaaabcbaabbcaacccababbcaabcbbbacbbbcaabbaaaccbbccccbcbbbacabaaaaacaabccaabcccaacba'
#                        'baabcbbcacbacabbacccabbaccbabaaacbcaabcbbcbaacaaabccabbbacaabaacbbbbccabbaaccabbbbbbcbaacb'
#                        'bccbcbcbababaaccbacccbbcabbbaaacbccbcbccaabccababbbbacabacacaccaaacbcbaaaacbcbcaabbbbcacbab'
#                        'aacccacbcccbbcbaccbaacccabcbbbaabaccbaaabccacacaacbaabbcaacaabbbaabaccacbcbbcccbacccaaaccacacb'
#                        'ccacabbccaabccacacacbccaaaacbabbcbcaaaaabbaacbcbbaabaabbccbbaaaabcbacabbbbcbbccacbcacabbbcbab'
#                        'cacababababaccbbacccaaccaccbacbbabbacbabaaacaabcbaaaabcccbbacaaaacbbccbbbbbcaabacbcaccbabccbbc'
#                        'acbbccbbabacbccaabbbaabacbabccabbbbcccabaab'
#                        'ccbccccabbccbcaabbaabccbcaacbcbbbbbabaccaaacbbaabccbccbaccaabcacaaacbbabaababababcccababcacaa'
#                        'bcbacbabcacababbbbccabbbcacbcbaabbbbbbacaaaacaccabbbbaacccacbcaacbcbbccbacbcacbaccbacabcbaacabb'
#                        'acbcccbccbcbbcbbbaaabacbaacbbaababbaaabbbbbbcbbabbbcbccacbcbaaccbcbccaacabcaccbabcaacbacabaab'
#                        'abacbcaabcbbabcbbaabbbccbabcbaccbacbbbcbabbbabbbccaacabccaaaaaccabaabbbaababaccaacbbacccbccacb'
#                        'accaacbcbaaacaccabccabccacccbcaaacaaaccacbaccccbacaaaaaabcaaacbbaabbbccbcbccbbacbbbbaabaabba'
#                        'cabccabcbaacaccbbcccbcbbccbacabbbcbcbbaccacbabcccaccabbcbbaccaaccabbccccaacacaacaccbabbbcabaaa'
#                        'bcbacaacaacbaacaacabbabcbcbbcbbccbabbabccbbbbababccaaaacbaabacbbccabacbbaaaacbaacbbbaacaaabac'
#                        'abbbabaaaaaabbabbacabcbcacbbabcbabbacaaacccbabbcaaaacabaccacaaaaacaccaacccbccbaccabcccccacabbc'
#                        'acaccacacabababababaccbbaaaaccabcbbaabbcababacaabcaaacacbcbcaccabbbcabaccbbabaababcaccacacbbcaa'
#                        'ccacbbccbaabcbcabcaabcbabcaacbabaaacaabacbcabbccbbcabaabbbbbabcaaaaabbbcabacbbababacbbcacbcbbc'
#                        'ccccaaabcacabacccaaabcacaccacabaacacaaacababacabaccbbabcaabcbacbbabcbaacccbcbccccaacabcbababcca'
#                        'baacaaabaaacabcacabbaaaaaccaabacaccababaaaaaabbcbbcbcaccccaabcbbabccbbaccbaaaababcaabcacbccaa'
#                        'accbacbabbcabbbbbababcccaccabaccbcaacbaccbcbccbbabbacaccbbbcbaaccaacccaaaabaabbbcbbbcaccccbbcc'
#                        'babccabbbabbcbbbaabccabacbaacaacccaacbbbbacbcaabaaaaccbacbbcbaabbccacbbbcbacbabbacccaacacccbbb'
#                        'aabbccbbbaccbaaabacbbbcbbbbbacbbbbaacaaccccbabaabcaabcacabaabbaaacababbacbccbbabbabbbabbbbabaca'
#                        'aabbbbbccccbabacabaacccbabaabbbababbabcabcbbabcbcbbcbcbcaaabbaaccabbbacacaacccccbbcbbcbabbbcbccb'
#                        'acccbaccabacbcabbbbbacccaacbbabcababaabbabcccabcbaccccbabaaaaaaacbcabbbababbcbcbccbbcaaccbcab'
#                        'bbabaabaacaccbbcccbccaaaacacbccbbbcbaaaaccaaaaaabbccaccaabbcbbaababcabbbccccbabcabacbacababbacb'
#                        'ccacbabaabcccbcbbccaccbabacbbccbbcaacacaabcaacbaacbaacabbaccaaabbabaacaccaaccacbacbbaaabbaabcca'
#                        'bbbbbabbbcabacbacbbaacabbbaacbbabcaccaaaabbaccababbbacbaccccccababcccacbbbaabbabbccccccbccbbaac'
#                        'ccaaaabbacacccbccabbbcccbcaacbabbaaacaaacbcacaccbababbbbccbcacbacccbaabcacbbbaccbbbcbccbcaccaabc'
#                        'abaaabcbcabbccacaaabbcbccbaabbaaacacbcaacccbcbcbacabcbbaacbaaaabcbbcacbbabcabbabbcaaaababcbaa'
#                        'bcccbbbcabbccbabcbbcaaabcaaacbcbbcabbbcbaacacabacaaabccacabaccaccacbaabcbcbbcccacaabbcaccbacbaa'
#                        'aacbacccbacbccacbabbbbabccbbcbaccbbacaccaccacbaabbcacaaabbaaacaabaacababaaabacbabcbacaacabbcacbbbcaacccbabaab'
#                        'cbbcacacbaabcacbbbaabbababababcbbbbccbabcacacaaacabcabcbcbacbcaaccacbcbcaabacabcbaaacbbbbbaccbc'
#                        'caaaabacccbbcccabaaacbcbaaccacabccacccccabcacacabbbabcaaaabcbbacaabacaaccacaacbaababbaacacbaacaccabbaab'
#                        'cbaabbccbccbbcbcbbaabbabbbbbcacaabaaabcbbcccbbcabcbbbcbacbaaccbbacbabccbccacabaaacccacbbaccbaacaabccaccacbacaabcbbcbbacabaaacacaccaabcccabaccbacabbbaacbaaccacbababbaaaabaacabacaacbbabcaabaccbcbbbbabcbbaaaaaabccbaccacbacbcaaabcccbbbbcabccbabaccbabacbcabbbbbacbcbaaaabbbabcaaacacccabbabbbbbcaccacbaccccbbacaabcabaaaccaccbccaaaabbababbbababacbabcabaabaabcbccccaaabbccaabacaabbbcccbabccbaabacbbbaaabacabcbbcaabbabbcbaacccbcbbcabacbabccbcccccccbbaaaaababbacaaacbcaacabccbaabaaabcbcccabaaccbabbaaccaabbcacabbabccaaabbcbcccccacbaaaabaaacbbaaacaabcabbaccbcacbabcabcccbbbaaaabbcbacabcccccabcbcacbccacbaaccba'
#                        'acaccabcbbcaaaabccccaaaaaabacccacabbbcbbcabccacbabaababcabcbaaabbcbaaaccbaabaaabcbbaabbcbaccabbbccacbbbacabaaabaaaccacaacbacbcbbaabcaabbbcbabcbbbbcbabbaccbbbbbccabaacbacacccbacabacbccbcaccabbbccccaabbaaacbaabacbbaaacabbbcabbbaccaacacacaaaaabbcaaabcaaabbccbabccaabbcbbcaaccbccbcbbbbababcabaabbacacaccbbacaccccccaccbbbcabbabacbbbccabbaaababcbcaacacbbabbccaacaabbaaaccaabcbbacabbababacacbccacbacbbabbacaabcbcabbaacbbbbcbcaabacacabbabcccaacbcabccbbbbcaccccacccacaccaaaacbbaaaacabaaaaaacabccaaacaaaabaacbaacbbbaabaacaabaacaaacbbaaacacbacbbabaacbbaccbacbccabaaacaacaaabcbccccabcacacbcbbbcbbbaabacaccccaccabacacabbbcbccbacaaacacacbaaabaacababacacaccbbaabaccccbcacbabbcaccbccacbcccbcacbbbaccabbbbcbbbac'
#                        'ccbaaacbccccbaccbabaabaacbcbbbaabacbbcbbbcbabbabcabccabcbbaabcbbacabbabbacabbccbbbbaccbabbccbbaabcbbccccabaaaccccbcaaaacccaacacbbcbbbaaaaacaaaaabbacabbccbabbccbaababbbacbbacbaaaacccaababcaccabaccaaacccbaabacbacbbbcbbbcbbccbcacaabaccaacbbccbccbabacacbbbbcacbaacccbccaabcabccbacccabbbcaacaabccacccacacaacbbbaccacccbbcbacabababcbabacacbabbccaacabcbbabbaaacbacbcacbbbbbcacbcacaabbabcbbcabaaccabaaacacabbbbcbbccabbbacacaaaccaabbbcbbacaabbbaccbcacabbabccbaabbcbabbbbcbbaabcabcbaccbbccabbbacabccccbbcbbbbaacaaaabaabccbcbbbcaacccabcbcbccaaaabaccbaaaacabbcacbcaabcacccccbcccaababbaabaaacabbaacbcbbbcababcbbcbbcbbccccabaaabccccccaabbbcacccbbcbbbbbbcbbbbabaccccbbacabbcbaaabbbbababaabbbcbabaacbcbabbaababaaaaabccaaabcaccccabcaccbaacccccaabcbcccaacabbbabaccacccabacbcbacaabccacaabbacccaccbaaaca'
#                        'cbbacccbbccbccabaabbacccbacacaccabcabbbabcaaccabcacccaacbabcabbbcbbcbacbbcbccccccbabbbaccbaaabacabbcaacbcaacbcbcacbbcbaccaccaaccbaabaacacaccccbabcabbaabbbacbcbbabbabbcabbcbcabcbacacbbcaacccabaacaacbbcaabbbbbaccababacccabcaabaaaacbbacbcccabcabccaaabccaacacbaacacaacbccaaababbcbcbcbcacacaabacbbbccbaacaacccccbbbccabcbacababbbcbcbcbccbbacbcccaaacaabaabccaababbbaccbbcbaabaabbbacbacaaccbacaabbacaccbbcbcaabcaaabaaaacaccbaccbbaccbabcbaccababccbacbcaaacbcbcabccbcbccbcccbabbcbaaaccbabcbbccbcbccccbbcccaabbbaaacbccaaacccccbcabaabaccbcbbabbccaababbbbaccbacbcbbcababbbcbccbcaabbabbababcccaaccacbacaacbabcbbcabccaabbcbaccabbabcaccaacccaaaabbabacbaabaabcbacaacbbbaabbababbaacbbcbabcaccbbacabcaaabaccccaaaccbacccbccccaaabbabacaacacabcaabcbccccbaacbbbcbcaaacbccccabbbbabbcbccaabbaabaaacaccbcacabcab'
#                         'baaacacbacabbababaaacbabcccbabaaabaacacaabacbcccbaccaabaccbaacbbbccbcbcbcccbcacbbccbacaaaaabbbaaaaccabacbabbabcaaaabbcbcacabcacbbabacbbbbcbacabbcbbcabccabacccaccbccbabcbcbabbcaaacabcbaacacacbaaacababbbcbaccaabaccbccababccbabacccbccabababcbbabaaaabaacabbbcbbbacbccaaccbbbcaaacccbacbabcacbaacaccabaabbcbcccbbccbba'))