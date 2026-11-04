class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        m=0
        for i in range(len(s)):
            s1=''
            for j in range(i+1,len(s)):
                s1=s[i:j+1]
                f=0
                for k in s1:
                    if s1.count(k)<=2:
                        f=1
                    else:
                        f=0
                        break
                if f==1:
                    if m<len(s1):
                        m=len(s1)
        return m