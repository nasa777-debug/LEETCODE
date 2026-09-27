class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        s=0
        if k==0:
            for i in range(len(nums)):
                a=str(bin(i))[2:]
                if a.count('1')==k:
                    s+=nums[i]
            return s    
        else:        
            for i in range(1,len(nums)):
                a=str(bin(i))[2:]
                if a.count('1')==k:
                    s+=nums[i]
            return s