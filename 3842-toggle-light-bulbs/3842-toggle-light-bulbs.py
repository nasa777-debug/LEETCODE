class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        l=[]
        for i in bulbs:
            if bulbs.count(i)==1 or bulbs.count(i)%2!=0:
                l.append(i)
        s=set(l)
        l1=list(s)
        l1.sort()
        return l1