class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        len_n = len(matrix)
        len_m = len(matrix[0])

        subsquares_represented = [[0 for _ in range(len_m)] for _ in range(len_n)]

        for r in range(len_n):
            for c in range(len_m):

                #case that matrix[r][c] == 0
                #then that matrix element cannot represent any subsquares, s_r[r][c] = 0
                if matrix[r][c] == 0:
                    subsquares_represented[r][c] = 0
                
                #border element, can never represent more than 1 square -> s_r[r][c] = 1
                elif matrix[r][c] == 1 and (r == 0 or c == 0):
                    subsquares_represented[r][c] = 1
                    
                #case that matrix[r][c] == 1
                #then matr. el. represents the minimum number of squares of its up and left neighbors + 1
                else:
                    up     = subsquares_represented[r-1][c]
                    left   = subsquares_represented[r][c-1]
                    upleft = subsquares_represented[r-1][c-1]
                    least_squares = min(up, left, upleft)

                    subsquares_represented[r][c] = least_squares + 1
        
        return sum([sum(x) for x in subsquares_represented])

                
