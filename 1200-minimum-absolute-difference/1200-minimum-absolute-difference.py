class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        m=float('inf')
        res=[]
        for i in range(1,len(arr)):
            diff=abs(arr[i-1]-arr[i])
            if diff<m:
                m=diff
                res=[[arr[i-1],arr[i]]]
            elif diff==m:
                res.append([arr[i-1],arr[i]])
        return res