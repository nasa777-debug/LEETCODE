class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        a,b=[],[]
        f=0
        for i in range(len(nums)):
            a=nums[:i+1]
            b=nums[i:]
            if max(a)-min(b)<=k:
                return i
                f=1
        if f==0:
            return -1