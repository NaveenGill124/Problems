## What I learned from Unique Paths

Given an \(m x n\) grid, any path from the top-left to the bottom-right consists of exactly:
\[
(m - 1)\text{ down-steps (D)} \quad\text{and}\quad (n - 1)\text{ right-steps (R)},
\]
for a total of
\[
(m - 1) + (n - 1) = m + n - 2
\]
moves.

### Example: \(2 \times 3\) Grid

- You need \(1\) down-step and \(2\) right-steps.
- Total moves: \(1 + 2 = 3\).
- The distinct sequences of moves are:
