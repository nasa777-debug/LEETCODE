class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr=[]
        nums.sort()
        a=0
        for i in range(len(nums)):
            if a!=len(nums):
                nums[a],nums[a+1]=nums[a+1],nums[a]
                a+=2
        return nums