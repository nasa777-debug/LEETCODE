class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        l=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        d=dict()
        ch='a'
        for i in range(len(l)):
            d[ch]=l[i]
            ch=chr(ord(ch)+1)
        r=[]
        for i in words:
            s=''
            for j in i:
                s+=d[j]
            r.append(s)
        return len(set(r))