Initially I came to the obvious brute force solution of checking every single potential square submatrix on its own, which would also take extremely long amounts of time as the dimensions of the original matrix grew. So I moved on from that idea relatively quickly.

I thought that the solution might involve working backwards from finding the largest possible squares, and using the mathematical relationship between a square of size n and how many subsquares exist within that complete square. The problem I ran into was attempting to track the rows and columns not encompassed by such squares.

I had a look at some hints about the programming task and after a bit of reading it seemed a lot like a problem I had taken on in an Algorithm Design class. The concept was similar to the idea that I had, wherein finding the largest possible square in a given area could also provide information about the subsquares of that square.
The idea that really elucidated the solution to me was being told to think about how to propogate the quantity of subsquares that a given matrix element represented using the up, left, and up-left elements.

Thinking about the smallest possible non-trivial subsquare (square of size 2), it can be seen more clearly how the value of a given element depends on those values. consider the following example, where we are trying to determine what value we should update the bottom right element to be.

| 1 | 0 |
|---|---|
| 1 | 1 |

we can see clearly that this 2x2 matrix does not represent a larger subsquare, and the way we prove that is by analyzing the minimum value of the adjacent up (U), left (L), and up-left (UL) elements. Even though the L and UL elements are 1, it is impossible to form a complete square since the U value is 0. Thus, we can update the value in the bottom right corner to that 0 value, plus 1 (representing the singleton element square).

| 1 | 1 |
|---|---|
| 1 | 1 |

When we do the same analysis for this 2x2 matrix, we can see via inspection that there is indeed a 2x2 subsquare. Taking the minimum of U, L, and UL will tell us that each of the necessary elements for a 2x2 subsquare are the proper value of 1, the minimum of them of course being 1. Thus, we can update the bottom right element to 1 (min of adj.) + 1 (singleton), giving a value of 2 for the element as it represents both itself as a singleton subsquare as well as the larger 2x2 subsquare up and to the left of it.

Finally, a quick analysis of how the algorithm scales.

| 1 | 1 | 1 |
|---|---|---|
| 1 | 2 | 2 |
| 1 | 2 | 1 |

when updating the bottom right element, we can see that its U, L, and UL elements are all 2 (thus the minimum is 2). These values show that there are complete 2x2 subsquares in each of the corners of the superior 3x3 subsquare, and when we find that the value of the bottom right is 1, we can add the minimum value to 1 to get a result of 3 for the bottom right element, representing the singleton element square, the 2x2 subsquare of its upper and left adjacent squares, and the 3x3 subsquare we know exists as a result of the existence of the 3 2x2 squares around the bottom right element.

once all matrix elements have been updated to show how many subsquares they represent, it is a simple matter of summing the values and returning the result.
