class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s=''
        y=0
        for i in nums:
            s+=str(i)
        for i in s:
            y+=int(i)
        return abs(sum(nums)-y)