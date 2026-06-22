class Solution:
    def isBalanced(self, num: str) -> bool:
        s1,s2=0,0
        for i in range(len(num)):
            if i%2==0:
                s1+=int(num[i])
            elif i%2!=0:
                s2+=int(num[i])
        if s1==s2:
            return True
        else:
            return False