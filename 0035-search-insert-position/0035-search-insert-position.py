class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        for i in range(len(nums)):
            j=i+1
            if j<len(nums):
                if target>nums[i] and target<nums[j]:
                    return j
        if target<min(nums):
            return 0
        elif target>max(nums):
            return len(nums)