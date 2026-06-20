class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split(' ')
        s1=''
        for i in l:
            s1+=i[::-1]+' '
        return s1.rstrip()