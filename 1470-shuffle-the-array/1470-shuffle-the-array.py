class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l1,l2=[],[]
        for i in range(len(nums)):
            if i<n:
                l1.append(nums[i])
            elif i>=n:
                l2.append(nums[i])
        l3=[]
        for i in range(n):
            l3.append(l1[i])
            l3.append(l2[i])
        return l3