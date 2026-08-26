class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[-1]*len(nums2)
        stack=[]
        for i in range(len(nums2)):
            while stack and nums2[i]>nums2[stack[-1]]:
                idx=stack.pop()
                ans[idx]=nums2[i]
            stack.append(i)
        l=[]
        d=dict()
        for i in range(len(nums2)):
            d[nums2[i]]=ans[i]
        for i in nums1:
            l.append(d[i])
        return l
