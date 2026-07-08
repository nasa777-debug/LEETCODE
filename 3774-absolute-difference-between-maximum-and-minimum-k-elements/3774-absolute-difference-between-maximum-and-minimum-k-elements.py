class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        a=sum(nums[0:k])
        nums.sort(reverse=True)
        b=sum(nums[0:k])
        return abs(a-b)