class Solution:
    def reverseByType(self, s: str) -> str:
        a,sp,r='','',''
        for i in s:
            if i.isalpha():
                a+=i
            else:
                sp+=i
        a=a[::-1]
        sp=sp[::-1]
        b,c=0,0
        for i in range(len(s)):
            if s[i].isalpha():
                r+=a[b]
                b+=1
            else:
                r+=sp[c]
                c+=1
        return r
