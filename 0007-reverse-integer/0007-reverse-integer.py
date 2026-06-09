class Solution:
    def reverse(self, x: int) -> int:
        s=str(x)
        if x>=0:
            if int(s[::-1])>(2**31):
                return 0
            return int(s[::-1])
        if x<0:
            s1=s[1:]
            if -1*int(s1[::-1])<((-2)**31):
                return 0
            return -1*int(s1[::-1])
        