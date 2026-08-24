class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        r=[]
        d1,d2=dict(),dict()
        for i in words:
            for j in range(len(i)):
                d1[i[j]]=pattern[j]
                d2[pattern[j]]=i[j]
            f=0
            for k in range(len(i)):
                if d1[i[k]]==pattern[k] and d2[pattern[k]]==i[k]:
                    f=1
                else:
                    f=0
                    break
            if f==1:
                r.append(i)
        return r