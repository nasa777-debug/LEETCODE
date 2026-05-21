class Solution:
    def mirrorDistance(self, n: int) -> int:
        x=str(n)
        return abs(n-int(x[::-1]))