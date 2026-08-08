class Solution:
    def isFascinating(self, n: int) -> bool:
        s='123456789'
        s1=str(2*n)
        s2=str(3*n)
        s3=str(n)
        s4=s3+s1+s2
        f=0
        for i in s:
            if len(s4)==len(s):
                if i in s4:
                    f=1
                else:
                    f=0
                    break
            else:
                f=0
                break
        return f==1