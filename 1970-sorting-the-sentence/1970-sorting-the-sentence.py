class Solution:
    def sortSentence(self, s: str) -> str:
        l=s.split(' ')
        for i in range(len(l)):
            for j in range(i+1,len(l)):
                if l[i][-1]>l[j][-1]:
                    l[i],l[j]=l[j],l[i]
        s1=''
        for i in l:
            s1+=i[:len(i)-1]+' '
        return s1.rstrip()