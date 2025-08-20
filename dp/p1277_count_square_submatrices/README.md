Initially I came to the obvious brute force solution of checking every single potential square submatrix on its own, which would also take extremely long amounts of time as the dimensions of the original matrix grew. So I moved on from that idea relatively quickly.

I thought that the solution might involve working backwards from finding the largest possible squares, and using the mathematical relationship between a square of size n and how many subsquares exist within that complete square. The problem I ran into was attempting to track the rows and columns not encompassed by such squares.

I had a look at some hints about the programming task and after a bit of reading it seemed a lot like a problem I had taken on in an Algorithm Design class. The concept was similar to the idea that I had, wherein finding the largest possible square in a given area could also provide information about the subsquares of that square.
