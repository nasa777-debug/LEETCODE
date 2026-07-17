class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        su=0
        for i in range(len(s)):
            su+=abs(s.index(s[i])-t.index(s[i]))
        return su