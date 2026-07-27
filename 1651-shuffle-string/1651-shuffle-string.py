class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d={}
        for i in range(len(s)):
            d[indices[i]]=s[i]
        r=''
        d1=dict(sorted(d.items()))
        for i in d1.keys():
            r+=d1[i]
        return r