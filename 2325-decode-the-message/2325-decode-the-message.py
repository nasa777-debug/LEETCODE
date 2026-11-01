class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d=dict()
        x='a'
        for i in key:
            if i not in d.keys() and i.isspace()==False:
                d[i]=x
                x=chr(ord(x)+1)
        res=''
        for i in message:
            if i==' ':
                res+=' '
            else:
                res+=d[i]
        return res