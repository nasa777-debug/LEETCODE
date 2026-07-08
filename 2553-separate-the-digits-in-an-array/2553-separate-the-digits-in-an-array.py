class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        l=[]
        for i in nums:
            if i>9:
                for j in str(i):
                    l.append(int(j))
            else:
                l.append(int(i))
        return l