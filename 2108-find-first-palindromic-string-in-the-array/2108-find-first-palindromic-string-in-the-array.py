class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        f=0
        for i in words:
            if i==i[::-1]:
                return i
                f=1
                break
            else:
                f=0
        if f==0:
            return ""