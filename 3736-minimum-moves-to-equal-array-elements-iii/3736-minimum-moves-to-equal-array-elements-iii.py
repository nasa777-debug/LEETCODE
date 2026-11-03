class Solution:
    def minMoves(self, nums: List[int]) -> int:
        c = 0
        for i in nums:
            c += max(nums) - i
        return c