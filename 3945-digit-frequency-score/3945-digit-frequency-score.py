class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        s=0
        for i in set(str(n)):
            s+=int(i)*(str(n).count(i))
        return s