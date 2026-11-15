class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        f=0
        for i in range(len(nums)):
            s=0
            for j in str(nums[i]):
                s+=int(j)
            if s==i:
                f=1
                break
            else:
                f=0
        if f==0:
            return -1
        else:
            return s