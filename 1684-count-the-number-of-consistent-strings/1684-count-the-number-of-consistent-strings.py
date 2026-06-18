class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c=0
        for i in words:
            f=0
            for j in i:
                if j in allowed:
                    f=1
                else:
                    f=0
                    break
            if f==1:
                c+=1
        return c