class Solution:
    def countCommas(self, n: int) -> int:
        c=0
        if n<1000:
            return 0
        for i in range(1000,n+1):
            c+=((len(str(i))-1)//3)
        return c