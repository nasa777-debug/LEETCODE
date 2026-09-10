class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        f=0
        for i in range(len(arr)):
            if 2*arr[i] in arr and arr.index(2*arr[i])!=i:
                f=1
                break
        return f==1