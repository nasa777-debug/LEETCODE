class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        d,nd=0,0
        for i in range(1,n+1):
            if i%m!=0:
                nd+=i
            else:
                d+=i
        return nd-d