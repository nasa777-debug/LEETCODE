class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        l=[]
        for i in words:
            for j in words:
                if j!=i:
                    if j in i:
                        l.append(j)
        return list(set(l))