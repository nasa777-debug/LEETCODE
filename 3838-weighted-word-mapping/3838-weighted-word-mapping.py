class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        d=dict()
        x='z'
        y=0
        while y<26:
            d[y]=x
            x=chr(ord(x)-1)
            y+=1
        d1=dict()
        r=''
        c='a'
        for i in weights:
            d1[c]=i
            c=chr(ord(c)+1)
        for i in words:
            s=0
            for j in i:
                s+=d1[j]
            r+=d[s%26]
        return r