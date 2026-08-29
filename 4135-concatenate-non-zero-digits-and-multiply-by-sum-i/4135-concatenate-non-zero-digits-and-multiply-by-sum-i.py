class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s=''
        l=0
        for i in str(n):
            if i!='0':
                s+=i
            l+=int(i)
        if s=='':
            return 0
        else:
            return int(s)*l