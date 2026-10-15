def isprime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
class Solution:
    def completePrime(self, num: int) -> bool:
        s=str(num)
        for i in range(1,len(s)+1):
            if not isprime(int(s[:i])):
                return False
        for i in range(len(s)):
            if not isprime(int(s[i:])):
                return False
        return True