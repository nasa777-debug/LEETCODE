class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l1,l2=[],[]
        for i in nums:
            if i<pivot:
                l1.append(i)
        for i in nums:
            if i>pivot:
                l2.append(i)
            if i==pivot:
                l1.append(i)
        return l1+l2