class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d={}
        for i in range(len(names)):
            d[heights[i]]=names[i]
        d1=dict(sorted(d.items(),reverse=True))
        l=[]
        for i in d1.values():
            l.append(i)
        return l