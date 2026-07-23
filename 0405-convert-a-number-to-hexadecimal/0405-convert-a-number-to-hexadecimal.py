class Solution:
    def toHex(self, num: int) -> str:
        if num>0:
            h=hex(num)
            return str(h)[2:]
        else:
            h1=hex(num & 0xFFFFFFFF)
            return str(h1)[2:]