class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        x=sorted(arr)
        res=[]
        d=dict()
        s=list(set(x))
        s.sort()
        for i in range(len(s)):
            d[s[i]]=i+1
        for i in arr:
            res.append(d[i])
        return res