class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        l=[]
        for i in tasks:
            l.append(sum(i))
        return min(l)