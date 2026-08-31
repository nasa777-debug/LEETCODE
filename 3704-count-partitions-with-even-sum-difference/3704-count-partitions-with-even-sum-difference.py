class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        c=0
        if sum(nums)%2!=0:
            return 0
        for i in range(len(nums)):
            if (sum(nums[:i])+sum(nums[i:]))%2==0:
                c+=1
        return c-1