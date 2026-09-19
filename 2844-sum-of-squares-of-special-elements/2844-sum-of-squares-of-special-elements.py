class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        a=[]
        s=0
        i=0
        a.append(0)
        while i!=len(nums):
            a.append(nums[i])
            i+=1
        for j in range(1,len(a)):
            if len(nums)%j==0:
                s+=a[j]**2
        return s