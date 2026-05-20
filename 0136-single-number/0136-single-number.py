class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x=0
        for i in nums:
            if nums.count(i)==1:
                x=i
        return x