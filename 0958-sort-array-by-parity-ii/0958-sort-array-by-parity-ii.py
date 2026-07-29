class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        o,e=[],[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                e.append(nums[i])
            else:
                o.append(nums[i])
        l=[]
        a,b=0,0
        for i in range(len(nums)):
            if i%2==0:
                l.append(e[a])
                a+=1
            else:
                l.append(o[b])
                b+=1
        return l 