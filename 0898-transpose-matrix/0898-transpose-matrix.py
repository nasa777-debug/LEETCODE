class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r=[]
        for i in range(len(matrix[0])):
            l=[]
            for j in range(len(matrix)):
                if j!=len(matrix):
                    l.append(matrix[j][i])
            r.append(l)
        return r