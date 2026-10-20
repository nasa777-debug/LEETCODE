class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s='abcdefghijklmnopqrstuvwxyz'
        f=0
        if len(set(sentence))<len(s):
            return False
        for i in set(sentence):
            if i in s:
                f=1
            else:
                f=0
                break
        return f==1