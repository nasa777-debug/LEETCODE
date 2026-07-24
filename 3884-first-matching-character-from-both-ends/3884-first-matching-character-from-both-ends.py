class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        x=-1
        f=0
        for i in range(len(s)):
            if s[i]==s[x]:
                return i
                f=1
                break
            else:
                f=0
            x+=-1
        if f==0:
            return -1