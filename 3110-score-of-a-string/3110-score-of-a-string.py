class Solution:
    def scoreOfString(self, s: str) -> int:
        s1=0
        i=0
        while i<len(s):
            j=i+1
            if j<len(s):
                s1+=abs(ord(s[i])-ord(s[j]))
            i+=1
        return s1