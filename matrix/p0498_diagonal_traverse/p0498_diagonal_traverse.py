class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        (m,n) = (len(mat), len(mat[0]))

        acc = [[] for _ in range(m + n - 1)]

        #fill diagonal arrays by index sum
        for i in range(m):
            for j in range(n):
                acc[i + j].append(mat[i][j])

        #reverse every other diagonal array
        for i in range(len(acc)):
            if not i % 2:
                acc[i].reverse()


        return [x for xs in acc for x in xs]
