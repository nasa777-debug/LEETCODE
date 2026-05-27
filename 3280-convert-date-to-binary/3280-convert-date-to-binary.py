class Solution:
    def convertDateToBinary(self, date: str) -> str:
        l=date.split('-')
        s1,s2,s3='','',''
        s1=l[0]
        s2=l[1]
        s3=l[2]
        s4=str(bin(int(s1)))[2:]+'-'+str(bin(int(s2)))[2:]+'-'+str(bin(int(s3)))[2:]
        return s4