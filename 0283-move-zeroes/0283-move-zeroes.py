class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=[]
        l1=[]
        for i in nums:
            if i==0:
                l.append(i)
            else:
                l1.append(i)
        nums.clear()
        for i in l1:
            nums.append(i)
        for i in l:
            nums.append(i)