class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        mi=0
        for i in sentences:
            l=i.split(' ')
            if len(l)>mi:
                mi=len(l)
        return mi