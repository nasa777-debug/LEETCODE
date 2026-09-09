class Solution:
    def countCommas(self, n: int) -> int:
        c=0
        threshold=1000
        while n>=threshold:
            c+=n-threshold+1
            threshold*=1000
        return c