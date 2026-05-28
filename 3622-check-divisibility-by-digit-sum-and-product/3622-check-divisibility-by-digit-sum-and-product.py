class Solution:
    def checkDivisibility(self, n: int) -> bool:
        p,s=1,0
        for i in str(n):
            p*=int(i)
            s+=int(i)
        if n%(p+s)==0:
            return True
        else:
            return False