class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        sys.set_int_max_str_digits(10**4)
        s=0
        for i in num:
            s=s*10+i
        s+=k
        l=[]
        for i in str(s):
            l.append(int(i))
        return l