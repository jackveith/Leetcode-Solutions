impl Solution {
    pub fn count_squares(matrix: Vec<Vec<i32>>) -> i32 {
        
        let len_n: usize = matrix.len();
        let len_m        = matrix[0].len();

        let mut represented_squares = vec![vec![0; len_m]; len_n];

        // loop over each element
        for r in 0..len_n {
            for c in 0..len_m {

            
                match matrix[r][c] {
                    0 => {/*noop, rep_sq[r][c] already 0*/}
                    1 => {
                        //edge case
                        if (r == 0 || c == 0) {
                            represented_squares[r][c] = 1;
                        }
                        //determine whether a larger square is formed by
                        //finding the minimum value of adj. elements
                        else {
                            let up     = represented_squares[r-1][c  ];
                            let left   = represented_squares[r  ][c-1];
                            let upleft = represented_squares[r-1][c-1];

                            represented_squares[r][c] = vec![up, left, upleft]
                            .iter()
                            .min()
                            .unwrap() + 1;
                        }
                    }
                    _ => println!("bad input."),
                }//end match
            }
        }//end iteration over matrix

        let ult_sum = represented_squares.iter().fold(0, |accum, row| {
            accum + row.iter().fold(0, |row_accum, &el| row_accum + el)
        });

        return ult_sum;

    }
}
