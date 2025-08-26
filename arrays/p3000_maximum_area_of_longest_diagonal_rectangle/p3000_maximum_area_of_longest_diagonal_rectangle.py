class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        
        ind = []
        maxd = 0
        for (i, dims) in zip(range(len(dimensions)), dimensions):

            #need not compare sqrt
            cd = dims[0]**2 + dims[1]**2

            #track new max diagonal
            if cd == maxd:
                ind[-1].append(i)
                continue

            #track same length diagonals as rect areas may differ
            if (cd > maxd):
                maxd = cd
                ind.append([i])

        return max([dimensions[i][0] * dimensions[i][1] for i in ind[-1]])

 
