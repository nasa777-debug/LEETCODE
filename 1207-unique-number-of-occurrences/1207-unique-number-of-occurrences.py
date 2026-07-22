class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        l=[]
        for i in set(arr):
            l.append(arr.count(i))
        if len(l)==len(set(l)):
            return True
        else:
            return False