class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        f=0
        for i in nums:
            if i!=max(nums):
                if max(nums)>=2*i:
                    f=1
                else:
                    f=0
                    break
        if f==1:
            return nums.index(max(nums))
        else:
            return -1