class Solution:
    def average(self, salary: List[int]) -> float:
        s=0
        salary.sort()
        s=sum(salary[1:len(salary)-1])
        return s/(len(salary)-2)