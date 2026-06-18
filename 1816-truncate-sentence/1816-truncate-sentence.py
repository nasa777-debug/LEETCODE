class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        l=s.split(' ')
        if len(l)==k:
            return s
        else:
            l=l[0:k]
            s1=''
            for i in l:
                s1+=i+' '
        return s1.rstrip()