class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        c=0
        l=text.split(' ')
        if brokenLetters=='':
            return len(l)
        for i in l:
            f=0
            for j in brokenLetters:
                if j not in i:
                    f=1
                elif j in i:
                    f=0
                    break
            if f==1:
                c+=1
        return c