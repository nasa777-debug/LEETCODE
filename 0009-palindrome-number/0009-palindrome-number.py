class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=0
        z=x
        if x<0 or (x%10==0 and x!=0):
            return False
        while(z>0):
            y=y*10+z%10
            z//=10
        if x==y:
            return True
        else:
            return False