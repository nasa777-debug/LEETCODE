class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        s=0
        a=[0]
        a+=nums
        for i in range(1,len(a)):
            if len(nums)%i==0:
                s+=a[i]**2
        return s