class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        l,l1=[],[]
        for i in set(nums):
            if nums.count(i)==2:
                l.append(i)
        return l[:2]