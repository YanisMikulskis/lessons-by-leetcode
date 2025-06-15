from collections import Counter
class Solution:
    '''
    Даны две строки: ransomNote и magazine.
    Вернуть true, если строку ransomNote можно собрать, используя буквы из строки magazine,
    и false в противном случае.
    Важно: Каждая буква из magazine может быть использована только один раз в ransomNote.
    '''
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_dict = Counter(ransomNote)
        magazine_dict = Counter(magazine)
        for let in ransom_dict:
            if let in magazine_dict:
                if magazine_dict[let] < ransom_dict[let]:
                    return False
            else:
                return False
        return True



sol = Solution()
print(sol.canConstruct('aa', 'aab'))
print(sol.canConstruct('a', 'aa'))


