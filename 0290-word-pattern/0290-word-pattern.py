class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l=s.split(' ')
        d1,d2=dict(),dict()
        if len(pattern)<len(l) or len(l)<len(pattern):
            return False
        elif len(pattern)==len(l):
            for i in range(len(pattern)):
                d1[pattern[i]]=l[i]
                d2[l[i]]=pattern[i]
            f=0
            for i in range(len(pattern)):
                if d1[pattern[i]]==l[i] and d2[l[i]]==pattern[i]:
                    f=1
                else:
                    f=0
                    break
            return f==1