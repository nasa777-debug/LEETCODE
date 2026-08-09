class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        s1,s2=0,0
        for i in str(n):
            s1+=int(i)
            s2+=int(i)**2
        return s2-s1>=50