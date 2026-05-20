class Solution:
    def romanToInt(self, s: str) -> int:
        r,c,p=0,0,0
        dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in range(len(s)-1,-1,-1):
            p=c
            if s[i] in dict.keys():
                c=dict[s[i]]
            if p>c:
                r-=c
            elif p<=c:
                r+=c
        return r