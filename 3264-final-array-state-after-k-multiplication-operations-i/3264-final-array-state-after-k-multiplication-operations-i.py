class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        x=min(nums)
        for i in range(1,k+1):
            nums[nums.index(x)]=x*multiplier
            x=min(nums)
        return nums