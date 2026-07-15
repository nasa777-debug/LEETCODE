class Solution:
    def maxProduct(self, n: int) -> int:
        l=[]
        for i in range(len(str(n))-1):
            for j in range(i+1,len(str(n))):
                l.append(int(str(n)[i])*int(str(n)[j]))
        return max(l)