class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        c=0
        l=sentence.split(' ')
        for i in l:
            if searchWord in i:
                if searchWord==i[:len(searchWord)]:
                    c=l.index(i)+1
                    break
        if c==0:
            return -1
        else:
            return c