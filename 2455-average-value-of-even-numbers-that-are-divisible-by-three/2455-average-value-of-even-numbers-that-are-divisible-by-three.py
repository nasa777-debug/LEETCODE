class Solution:
    def averageValue(self, nums: List[int]) -> int:
        l=[]
        for i in nums:
            if i%2==0 and i%3==0:
                l+=[i]
        if len(l)!=0:
            return sum(l)//len(l)
        elif len(l)==0:
            return 0