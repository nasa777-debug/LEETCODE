class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses=Counter()
        players=set()
        for i,j in matches:
            players.add(i)
            players.add(j)
            losses[j]+=1
        zl,ol=[],[]
        for i in players:
            if losses[i]==1:
                ol.append(i)
            elif losses[i]==0:
                zl.append(i)
        return [sorted(zl),sorted(ol)]