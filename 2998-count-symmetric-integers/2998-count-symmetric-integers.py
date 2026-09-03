class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        c=0
        for i in range(low,high+1):
            l=[]
            for j in str(i):
                l.append(int(j))
            if len(l)%2==0:
                if sum(l[:len(l)//2])==sum(l[len(l)//2:]):
                    c+=1
        return c