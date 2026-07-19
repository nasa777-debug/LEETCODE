class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        o,e,r=[],[],[]
        for i in range(len(nums)):
            if i%2==0:
                e.append(nums[i])
            else:
                o.append(nums[i])
        e.sort()
        o.sort(reverse=True)
        o1,e1=0,0
        for i in range(len(nums)):
            if i%2==0:
                r.append(e[e1])
                e1+=1
            else:
                r.append(o[o1])
                o1+=1
        return r