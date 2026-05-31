class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge=nums1+nums2
        merge.sort()
        a=0
        b=len(merge)-1
        m=(a+b)//2
        if len(merge)%2==0:
            return float((merge[m]+merge[m+1])/2)
        else:
            return float(merge[m])