class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        r=''
        f=0
        for i in range(len(s)):
            r=s[i+1:]+s[0:i+1]
            if r==goal:
                f=1
                break
            else:
                f=0
        return f==1   