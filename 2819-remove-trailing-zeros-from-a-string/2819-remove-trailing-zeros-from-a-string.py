class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        ans=''
        i=-1
        while num[i]=='0':
            i+=-1
        if i==-1:
            return num
        ans=num[:i+1]
        return ans