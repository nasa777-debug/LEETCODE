class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        l=[i for i in arr if arr.count(i)==1]
        f=0
        for i in range(len(l)):
            if i==k-1:
                return l[i]
                f=1
            else:
                f=0
        if f==0:
            return ''
