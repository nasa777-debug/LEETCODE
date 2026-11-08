class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        l=[]
        for i in range(1,len(nums)+10):
            l.append(k*i)
        for i in nums:
            if i%k!=0:
                nums.remove(i)
        for i in l:
            if i not in nums:
                return i