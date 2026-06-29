class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        c=0
        for i in nums:
            if i<k:
                c+=1
        return c