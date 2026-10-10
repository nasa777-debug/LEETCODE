class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        l=[]
        for i in nums:
            if i%2==0:
                l.append(i)
        if l==[]:
            return -1
        r=[]
        m=0
        l.sort()
        for i in l:
            if l.count(i)>m:
                m=l.count(i)
        for i in set(l):
            if l.count(i)==m:
                r.append(i)
        return min(r)