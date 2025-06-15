class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:

        return [i[0] for i in enumerate(words) if x in i[1]]


print(func(['abc', 'bcd', 'aaaa', 'cbc'], x = 'a'))