class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        c=0
        for i in range(len(nums)-1):
            while nums[i]<nums[-1]:
                nums[i]+=1
                c+=1
        return c