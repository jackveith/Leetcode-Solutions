class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        
        len_m = len(mat)
        len_n = len(mat[0])

        N_VAL = 0
        M_VAL = 1
        RECTS = 2

        #             N, M, rects
        rep_rects = [[(0, 0, 0) for _ in range(len_n)] for _ in range(len_m)]

        for r in range(len_m):
            for c in range(len_n):

                if mat[r][c] == 0:
                    continue
                
                #mat value is 1, determine M and N values.
                #determined by adjacent left and right elements of the rep_rects matr.
                #unless border block, then find what border(s) to determine M and N.
                elif r == 0 or c == 0:
                    match (r,c):
                        case (0,0):
                            rep_rects[r][c] = (0, 0, 1)
                        #row is 0
                        case (0, _):
                            #if there are 1's left, add 1 to its consec_1 length. else it is 0, thus 0
                            new_n = rep_rects[0][c-1][N_VAL] + 1 if mat[r  ][c-1] == 1 else 0
                            #the represented rectangles will be the extension of the new_n rects
                            #to the left, and itself (+1)
                            rep_rects[r][c] = (new_n, 0, new_n + 1)

                        #col is 0
                        case (_, 0):
                            #if there are 1's upwards, add 1 to its consec_1 length. else it is 0, thus 0
                            new_m = rep_rects[r-1][0][M_VAL] + 1 if mat[r-1][c  ] == 1 else 0
                            #the represented rectangles will be the extension of the new_m rects
                            #upward, and itself (+1)
                            rep_rects[r][c] = (0, new_m, new_m + 1)

                        case (_, _):
                            pass

                #not a border block. iterate and find how many rectangles will be extended.
                else:
                    #first calculate the M and N values
                    new_n = rep_rects[r  ][c-1][N_VAL] + 1 if mat[r  ][c-1] == 1 else 0
                    new_m = rep_rects[r-1][c  ][M_VAL] + 1 if mat[r-1][c  ] == 1 else 0

                    #maximum potential upleft lookback
                    max_lookback = min(new_n, new_m)
                    max_left = new_n - 1
                    max_up   = new_m - 1
                    dist = 1

                    rep_rects_el = 1 + new_m + new_n
                    curr_upleft = rep_rects[r-1][c-1]

                    while max_lookback > 0:
                        max_lookback -= 1

                        
                        
                        #0 up and left
                        if curr_upleft[RECTS] > 0:
                            rep_rects_el += 1

                            rep_rects_el += min(max_left, curr_upleft[N_VAL])
                            max_left = min(max_left - 1, curr_upleft[N_VAL])

                            rep_rects_el += min(max_up, curr_upleft[M_VAL])
                            max_up = min(max_up - 1, curr_upleft[M_VAL])

                            if max_up == 0 or max_left == 0:
                                break 

                        else:
                            break


                        if max_lookback > 0:
                            dist += 1
                            curr_upleft = rep_rects[r-dist][c-dist]

                    rep_rects[r][c] = (new_n, new_m, rep_rects_el)

        return sum([sum([x for (_, _, x) in row]) for row in rep_rects])





                #find the maximum extension of the rectangle for both 
                #the x and y axes
