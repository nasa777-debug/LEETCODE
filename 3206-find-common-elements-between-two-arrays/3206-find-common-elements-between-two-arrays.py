class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        c=0
        for i in nums1:
            if i in nums2:
                c+=1
        l.append(c)
        c=0
        for i in nums2:
            if i in nums1:
                c+=1
        l.append(c)
        return l