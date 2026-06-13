class Solution:
    def maxFreqSum(self, s: str) -> int:
        c,c1=0,0
        for i in s:
            if i in ['a','e','i','o','u','A','E','I','O','U']:
                if s.count(i)>c:
                    c=s.count(i)
            elif i not in ['a','e','i','o','u','A','E','I','O','U'] and i.isalpha():
                if s.count(i)>c1:
                    c1=s.count(i)
        return c+c1