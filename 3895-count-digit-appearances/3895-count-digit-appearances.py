class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        c = 0
        for i in nums:
            for j in str(i):
                if int(j) == digit:
                    c += 1
        return c