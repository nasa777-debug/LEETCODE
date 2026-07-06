class Solution:
    def countSegments(self, s: str) -> int:
        c=0
        l=s.split()
        for i in l:
            if i=='':
                pass
            else:
                c+=1
        return c