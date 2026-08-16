class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        l,r=0,len(nums)-1
        nums.sort()
        avg=[]
        while l<=r:
            avg.append((nums[l]+nums[r])/2)
            l+=1
            r-=1
        return min(avg)
