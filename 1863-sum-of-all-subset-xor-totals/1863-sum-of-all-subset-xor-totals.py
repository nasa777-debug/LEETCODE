from itertools import combinations
class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        l=[]
        for i in range(len(nums)):
            for j in combinations(nums,i):
                l.append(list(j))
        l.append(nums)
        s=0
        for i in l:
            if i!=[]:
                x=0
                for j in i:
                    x^=j
                s+=x
        return s