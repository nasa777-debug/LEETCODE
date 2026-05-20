class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x=int(a,2)
        y=int(b,2)
        z=bin(x+y)
        s=str(z)
        return s[2:]