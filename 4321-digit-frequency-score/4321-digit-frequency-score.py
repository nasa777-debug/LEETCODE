class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        s=0
        for i in str(n):
            s+=int(i)
        return s
        