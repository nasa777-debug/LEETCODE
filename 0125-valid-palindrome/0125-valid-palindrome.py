class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=''
        for i in s.lower():
            if i.isalpha() or i.isdigit():
                s1+=i
        return s1==s1[::-1]