class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote)==len(magazine):
            f=0
            for i in magazine:
                if i in ransomNote:
                    f=1
                else:
                    f=0
                    break
            return f==1
        elif len(ransomNote)<len(magazine):
            f=0
            for i in ransomNote:
                if i in magazine and ransomNote.count(i)<=magazine.count(i):
                    f=1
                else:
                    f=0
                    break
            return f==1
        else:
            return False