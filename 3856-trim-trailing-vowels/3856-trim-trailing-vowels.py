class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        i=len(s)-1
        while s[i] in 'aeiou' and i!=-1:
            i+=-1
        return s[:i+1]