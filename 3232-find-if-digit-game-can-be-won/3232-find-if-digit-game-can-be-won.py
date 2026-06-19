class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        l1,l2,l3,l4=[],[],[],[]
        for i in nums:
            if len(str(i))>1:
                l2.append(i)
                l3.append(i)
            else:
                l1.append(i)
                l4.append(i)
        if sum(l1)>sum(l2) or sum(l3)>sum(l4):
            return True
        else:
            return False