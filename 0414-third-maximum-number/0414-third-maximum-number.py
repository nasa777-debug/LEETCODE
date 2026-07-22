class Solution:
    def thirdMax(self, nums: List[int]) -> int:
            nums1=set(nums)
            nums2=list(nums1)
            nums2.sort(reverse=True)
            if len(nums2)<=2:
                return max(nums2)
            elif len(nums2)==3:
                return min(nums2)
            else:
                return nums2[2]