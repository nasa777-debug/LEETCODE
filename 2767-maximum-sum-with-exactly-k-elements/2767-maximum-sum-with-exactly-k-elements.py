class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        s=0
        nums.sort()
        for i in range(k):
            a=nums.pop()
            s+=a
            nums.append(a+1)
        return s