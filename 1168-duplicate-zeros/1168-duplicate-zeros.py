class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        l=[]
        for i in arr:
            if i!=0:
                l.append(i)
            elif i==0:
                l.append(i)
                l.append(0)
        l=l[:len(arr)]
        arr.clear()
        arr+=l