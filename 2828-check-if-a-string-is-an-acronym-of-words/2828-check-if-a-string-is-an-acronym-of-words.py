class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        s1 = ''
        for i in words:
            s1 += i[0]
        return s1 == s