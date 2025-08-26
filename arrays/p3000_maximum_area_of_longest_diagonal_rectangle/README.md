### Solution
Pretty simple problem to solve, by iterating over the array and keeping track of the rectangles that have the longest diagonal (as rectangles with equal diagonals do not necessarily have the same area). There are some small efficiency improvements to be made, by saving certain calculations for later:

We realize that we do not need to calculate the actual diagonal in the iteration, as the sum of the each dimension squared,  `curr_x^2 + curr_y^2`, will always have the same relationship to `best_rect_x^2 + best_rect_y^2` as `sqrt(curr_x^2 + curr_y^2)` will have to `sqrt(best_rect_x^2 + best_rect_y^2)`.

The calculation of the area of the longest rectangles can also be saved until the very end, where we will only need to find the area of the rectangle(s) which has the longest diagonal.

Something I realized after solving that could improve my solutions memory efficiency is that we do not care about rectangles with smaller diagonals once we have found a rectangle with a larger one, even if their area may be larger. Therefore, instead of appending a new list to my accumulator matrix when I find a larger diagonal, I can simply overwrite a 1D list every time I find a longer diagonal and append to that list if I find a a rectangle with an equivalent diagonal.

### Hints
I constructed some socratic hints and ideas for my peers:
- how should we keep track of the largest diagonal we have found, and how should we keep track of the rectangle it represents?

- Is it possible for two rectangles which have the same length diagonal to have different areas? If so, how do we make sure that we return the largest area between those rectangles?

##### Ideas related to questions
- ideas for keeping track of the longest diagonal:
  - we can track the length of the longest diagonal, and update it when we find a new longest diagonal
  - we can track the length of each rectangle's diagonal and store it with information about the rectangle, then find which rectangle(s) have the longest diagonal

- ideas for keeping track of the rectangle:
  - we can track the rectangle by finding its area and storing it,
  - we can track the rectangle by storing its dimensions from the array,
  - we can track the index of where that rectangle is in the array, to get its dimensions and calculate the area later

- Can 2 or more rectangles have equal diagonals, but inequal areas?
  - yes they can, so we must make sure to track each rectangle that has the (current) longest diagonal, then find which one has the largest area, so we can return that area.
