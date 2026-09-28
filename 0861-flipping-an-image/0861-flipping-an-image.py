class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        l=[]
        for i in image:
            r=i[::-1]
            s=[]
            for j in r:
                if j==0:
                    s.append(1)
                elif j==1:
                    s.append(0)
            l.append(s)
        return l