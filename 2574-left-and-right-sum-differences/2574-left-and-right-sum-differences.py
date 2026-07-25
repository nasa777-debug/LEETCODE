class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        l=[]
        r=[]
        for i in range(len(nums)):
            l.append(sum(nums[:i]))
            r.append(sum(nums[i+1:]))
        s=[]
        for i in range(len(nums)):
            s.append(abs(l[i]-r[i]))
        return s