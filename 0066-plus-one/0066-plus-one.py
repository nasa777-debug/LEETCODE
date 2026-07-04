class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=''
        for i in digits:
            s+=str(i)
        x=int(s)
        x+=1
        s1=str(x)
        l=[]
        for i in s1:
            l.append(int(i))
        return l