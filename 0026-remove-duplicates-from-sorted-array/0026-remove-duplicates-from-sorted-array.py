class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=list(set(nums))
        nums.clear()
        l.sort()
        nums+=l
        return len(nums)