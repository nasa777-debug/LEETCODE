class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d=Counter(s)
        l=[]
        for i in d.values():
            l.append(i)
        return len(set(l))==1