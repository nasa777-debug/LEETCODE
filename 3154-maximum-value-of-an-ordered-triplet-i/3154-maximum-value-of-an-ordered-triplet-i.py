class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        l=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if (nums[i]-nums[j])*nums[k]>0:
                        l.append((nums[i]-nums[j])*nums[k])
        if l==[]:
            return 0
        else:
            return max(l)