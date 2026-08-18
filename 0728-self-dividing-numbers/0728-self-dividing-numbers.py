class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        r=[]
        for i in range(left,right+1):
            f=0
            for j in str(i):
                if j!='0':
                    if i%int(j)==0:
                        f=1
                    else:
                        f=0
                        break
                else:
                    f=0
                    break
            if f==1:
                r.append(i)
        return r