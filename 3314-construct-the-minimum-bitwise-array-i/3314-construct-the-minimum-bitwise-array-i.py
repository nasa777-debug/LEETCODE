class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        r=[]
        for i in nums:
            f=0
            for j in range(1,i):
                if j|j+1 == i:
                    r.append(j)
                    f=1
                    break
            if f==0:
                r.append(-1)
        return r