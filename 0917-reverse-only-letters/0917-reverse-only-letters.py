class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        a=''
        for i in s:
            if i.isalpha():
                a+=i
        a=a[::-1]
        r=''
        j=0
        for i in range(len(s)):
            if s[i].isalpha():
                r+=a[j]
                j+=1
            else:
                r+=s[i]
        return r