class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            x=word.index(ch)
            return word[x::-1]+word[x+1:]
        else:
            return word