class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:

        (m,n) = (len(mat), len(mat[0]))
        acc = 0

        row_length = [[0 for _ in range(n)] for _ in range(m)]


        for r in range(m):
            for c in range(n):
                if  c == 0:
                    row_length[r][0] = mat[r][0]
                else:
                    row_length[r][c] = row_length[r][c-1] + 1 if mat[r][c] else 0

        for r in range(m):
            for c in range(n):
                if row_length[r][c] == 0:
                    pass
                else:
                    max_rects = row_length[r][c]
                    for curr_r in range(r, -1, -1):
                        max_rects = min(max_rects, row_length[curr_r][c])
                        if max_rects == 0:
                            break
                        acc += max_rects

        print(row_length)
        return acc

