class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxsum=0
        for i in accounts:
            if sum(i)>maxsum:
                maxsum=sum(i)
        return maxsum