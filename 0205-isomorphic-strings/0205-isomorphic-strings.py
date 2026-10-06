class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1,d2=dict(),dict()
        if len(s)<len(t) or len(t)<len(s):
            return False
        elif len(s)==len(t):
            f=0
            for i in range(len(s)):
                d1[s[i]]=t[i]
                d2[t[i]]=s[i]
            for i in range(len(s)):
                if d1[s[i]]==t[i] and d2[t[i]]==s[i]:
                    f=1
                else:
                    f=0
                    break
            return f==1