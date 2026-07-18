class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l=sorted(s)
        p=sorted(t)
        return l==p