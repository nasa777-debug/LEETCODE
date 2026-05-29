class Solution:
    def minElement(self, nums: List[int]) -> int:
        l=[]
        for i in nums:
            s=0
            for j in str(i):
                s+=int(j)
            l.append(s)
        return min(l)