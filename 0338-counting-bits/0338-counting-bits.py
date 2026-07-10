class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[]
        for i in range(0,n+1):
            x=str(bin(i))
            l.append(x.count('1'))
        return l