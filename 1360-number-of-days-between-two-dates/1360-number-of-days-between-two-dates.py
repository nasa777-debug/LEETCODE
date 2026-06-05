class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        l=date1.split('-')
        l1=date2.split('-')
        d1=date(int(l[0]),int(l[1]),int(l[2]))
        d2=date(int(l1[0]),int(l1[1]),int(l1[2]))
        if d1>d2:
            d1,d2=d2,d1
        diff=d2-d1
        return diff.days