class Solution:
    def findGCD(self, nums: List[int]) -> int:
        x=min(nums)
        y=max(nums)
        while x!=0:
            r=y%x
            y=x
            x=r
        return y 