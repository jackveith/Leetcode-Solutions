### Attempt 1

I overthought this problem way too hard in the beginning, trying to traverse each diagonal of the matrix in the correct order by using separate subroutines for the shorter triangular diagonal sets in the corners, as well as for the "square" diagonals that were of length equal to the constraining/shorter side of the matrix. These took arguments such as the initial direction of the traversal, the length of the triangle/number of square diagonals, and the accumulator array that would be mutated and returned. It took a lot of thinking about how to keep track of the actual indices of the original matrix to retrieve the correct values, as well as creating nested `for` loops for iterating in different directions; this solution was quite inelegant.

### Solution
I checked out the discussion of the question because I wanted to find a better solution without looking at a real writeup or code. This comment gave me an epiphany:

"Hint: you can group the elements in each diagonal by the sum of their indices."

I had started making a quick diagram for myself before I had started programming, and returned to it for a moment to draw out some indices and sums before quickly returning to a new solution. I figured out that there would be as many diagonals as the sum of `m` and `n` minus $1$ for any `m`x`n` matrix. Then it was as simple as sorting each element into its respective array based on the sum of its indices as I traversed over the matrix by row and column. The only other issue that I had was trying to use a list comprehension to selectively flip the subarrays representing the diagonals of the matrix, because I was attempting to place the return value of `subarray.reverse()` (`None`) into the final flattened array, which caused me to doubt the iteration and array filling logic. I found the issue, modified the subarrays in place in a `for` loop, then returned the flattened array of diagonals with a list comprehension. 

### Diagram
I started working on a diagram for a moment before jumping into programming; I wish I would've spent a bit more time on it to find the simple solution. After returning from the hint, I filled in about half of the rightmost square matrix with (row, col, sum) tuples before hopping back into the code and solving. 

In order to make a better hint diagram for my friends, I filled out the rest of the larger matrix with (row, col, sum) tuples. Additionally, I made a few more example matrices, for the `len(mat) == 1` case, as well as `2`x`4` and `4`x`2` matrices to demonstrate behavior for matrices where `m != n`. A splash of color and directional arrows like were shown in the problem description helped make the relationship between the diagonals and the sum of an element's indices much clearer.
