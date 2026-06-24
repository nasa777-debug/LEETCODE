class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c=0
        for i in nums:
            if i%3==0:
                pass
            elif i%3!=0:
                i+=1
                c+=1
        return c