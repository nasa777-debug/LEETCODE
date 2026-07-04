class Solution:
    def capitalizeTitle(self, title: str) -> str:
        s=''
        l=title.split(' ')
        for i in l:
            if len(i)<=2:
                s+=i.lower()
                s+=' '
            else:
                s+=i.title()
                s+=' '
        return s.rstrip()