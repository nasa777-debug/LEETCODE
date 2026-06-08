class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        if k==len(s):
            return s[::-1]
        else:
            return s[k-1::-1]+s[k:]